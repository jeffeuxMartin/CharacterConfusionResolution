#!python3
import sys
import re
import json
from pathlib import Path
from typing import List, Tuple, Union, TextIO
from collections import defaultdict

from tqdm import tqdm

audio_Codes = [
    "jyutping",
    "bopomofo",
    "pinyin",

    "cantonhk",
    "cnsphoneticlite",
    "ile",
    "jyutping0",
    "roman",
    "zyujam",
]

visualCodes = [
    "cj5",
    "boshiamy",
    "dayi4",
    "4corner5",
    
    "3corner",
    "4corner",
    "array10",
    "array30",
    "array40",
    "bsm",
    "cangjie",
    "ckc",
    "dayi2",
    "dayi3",
    "dna",
    "ejcj",
    "ez",
    "freenewcj",
    "g6code",
    "hs",
    "mscj3",
    "newcj3",
    "qcode",
    "scj6",
    "simplecj",
    "simplex",
    "simplex5",
    "stroke5",
    "strokes",
    "uniliu",
    "whale",
    "wm2",
]

def cin_parser(
    fname: Union[str, Path], 
    ferr: TextIO,
  ) -> Tuple[dict, dict]:
    code2term, term2code = {}, {}
    with open(fname) as f:
        running = False
        for line_idx, line_raw in enumerate((f)):
            line = line_raw.strip("\n")
            if line == r"%chardef end":
                running = False
            if running:
                try:
                    key, value = re.split(
                        r" +|\t+|\u3000+", line, 
                        maxsplit=1)
                except ValueError as err:
                    print(
                        "Parsing error for "
                        "{:25s}:{:7d} (skipped)"
                        "--> {}".format(
                            str(cin), line_idx + 1,
                            line.__repr__(),
                    ), file=ferr)
                    continue
                if key not in code2term:
                    code2term[key] = []
                code2term[key].append(value)
                if value not in term2code:
                    term2code[value] = []
                term2code[value].append(key)
            if line == r"%chardef begin":
                running = True
    return code2term, term2code

def depack(list_of_str: List[str]) -> Union[List[str], str]:
    if len(list_of_str) == 1:
        return ' ' + repr(list_of_str[0])
    return list_of_str
    
def chinese_code_gather(zh_charset, fname):
    with open(f'{fname}.yaml', 'w') as f:
        for z in tqdm(zh_charset):
            print(f'{z}:', file=f)
            if 'frequency' in zh_charset[z]:
                [freq] = zh_charset[z]['frequency']
                freq = int(freq)
                print(f'    frequency: {freq:6d}', file=f)
            else:
                freq = 'NaN'
                print(f'    frequency:  "NaN"', file=f)
            
            print('    audio:', file=f)
            for coding_method in audio_Codes:
                if coding_method in zh_charset[z]:
                    print("        {met:{maxlen}}: {cod}".format(
                        met=coding_method,
                        cod=depack(zh_charset[z][coding_method]),
                        maxlen=maxlen_au + 1,
                    ), file=f)
            print(file=f)

            print('    visual:', file=f)
            for coding_method in visualCodes:
                if coding_method in zh_charset[z]:
                    print("        {met:{maxlen}}: {cod}".format(
                        met=coding_method,
                        cod=depack(zh_charset[z][coding_method]),
                        maxlen=maxlen_vi + 1,
                    ), file=f)
            print(file=f)

            print(file=f)

    import yaml
    with open(f"{fname}.yaml", "r") as f:
        data = yaml.load(f, Loader=yaml.SafeLoader)


    import json
    with open(f"{fname}.json", "w") as f:
        json.dump(data, f,
            ensure_ascii=False, indent=4)

    # import json
    # with open(f"{fname}.json", "r") as f:
    #     data = json.load(f)

if __name__ == "__main__":    
    cins = list(Path("cin-tables").glob("*.cin"))
    cins = [Path("cin-tables") / (cin + '.cin')
        for cin in (
            audio_Codes + visualCodes + ['frequency'])]

    with open("errors.log", "w") as ferr:
        all_code2terms, all_term2codes = {}, {}
        for cin in cins:  # tqdm
            cin_key = re.sub(r"\.cin$", "", cin.name)

            (all_code2terms[cin_key], 
             all_term2codes[cin_key]) = (
                cin_parser(cin, ferr))

    merged_term2code = defaultdict(defaultdict)
    for cin, term2codedic in (
            all_term2codes.items()):  # tqdm
        for hanterm in term2codedic:
            merged_term2code[hanterm][cin] = (
                term2codedic[hanterm])
    
    char2code, word2code = {}, {}
    for term in sorted(merged_term2code):
        (char2code 
             if len(term) == 1 else 
         word2code)[term] = merged_term2code[term]

    with open("charcode_table.json", "w") as f:
        json.dump(char2code, f, 
            ensure_ascii=False, indent=4)
            
    with open("charset.txt", "w") as f_charset, \
         open("wordset.txt", "w") as f_wordset:
        print('\n'.join(char2code), file=f_charset)
        print('\n'.join(word2code), file=f_wordset)
    
    with open('ord_chartable.tsv', 'w') as f:
        maxlen = len(str(ord(max(char2code))))
        print(f"{'ord':{maxlen}s}\tcharacter", file=f)
        for hanchar in sorted(char2code):
            print(f"{ord(hanchar):{maxlen}d}\t"
                  f"{hanchar}", file=f)
    
    # pd.read_csv("ord_chartable.tsv", 
    #     sep="\t", quoting=csv.QUOTE_NONE)
    
    for b in [1, 2, 3]:
        with open(f'char{b}byte.txt', 'w') as f:
            f.write("".join([
                c for c in char2code 
                if 2 ** (8 * (b - 1)) 
                    <= ord(c) 
                    < 2 ** (8 * b)]))

    # import json
    # with open('charcode_table.json') as f:
    #     char2code = json.load(f)

    # 19968	一
    # 40943	鿯
    zh2code = {c: char2code[c] 
        for c in char2code 
        if 19968 - 1 < ord(c) < 40943 + 1}

    with open(
        "regular_zhcharcode_table.json", "w") as f:
        json.dump(zh2code, f, 
            ensure_ascii=False, indent=4)
            

  
        
    # === NOTE === #
    # 1. According to Eric, 應該有 123,928 個「全形漢字」？
    # >>> 2127396 char_lexicon.json
    # >>> 9148527 full.json
    # 2. ( ??? ) 如果只有「一碼」要不要用成 string?
    # 3. (Todo!) 移除掉詞語！




    maxlen_au = len(max(audio_Codes, key=len))
    maxlen_vi = len(max(visualCodes, key=len))
    

    unicode_char2code = {c: char2code[c] 
        for c in char2code 
        # if 2 ** 8 <= ord(c)
        if 11904 <= ord(c)  # if ord('⺀') <= ord(c)
    }

    chinese_code_gather(
        unicode_char2code, "full_zh_charset")
