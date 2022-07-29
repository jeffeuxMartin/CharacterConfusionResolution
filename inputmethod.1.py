#!python3
import sys
import re
import json
from pathlib import Path
from typing import Tuple, Union, TextIO
from collections import defaultdict

from tqdm import tqdm


def cin_parser(
    fname: Union[str, Path], 
    ferr: TextIO,
  ) -> Tuple[dict, dict]:
    code2char, char2code = {}, {}
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
                if key not in code2char:
                    code2char[key] = []
                code2char[key].append(value)
                if value not in char2code:
                    char2code[value] = []
                char2code[value].append(key)
            if line == r"%chardef begin":
                running = True
    return code2char, char2code


if __name__ == "__main__":    
    cins = list(Path("cin-tables").glob("*.cin"))

    with open("errors.log", "w") as ferr:
        all_code2chars, all_char2codes = {}, {}
        for cin in cins:  # tqdm
            cin_key = re.sub(r"\.cin$", "", cin.name)

            (all_code2chars[cin_key], 
             all_char2codes[cin_key]) = (
                cin_parser(cin, ferr))

    merged_char2code = defaultdict(defaultdict)
    for cin, char2codedic in (
            all_char2codes.items()):  # tqdm
        for hanchar in char2codedic:
            merged_char2code[hanchar][cin] = (
                char2codedic[hanchar])

    with open("full.json", "w") as f:
        json.dump(merged_char2code, f, 
            ensure_ascii=False, indent=4)

# === NOTE === #
# 1. According to Eric, 應該有 123,928 個「全形漢字」？
# >>> 2127396 char_lexicon.json
# >>> 9148527 full.json
# 2. ( ??? ) 如果只有「一碼」要不要用成 string?
# 3. (Todo!) 移除掉詞語！
