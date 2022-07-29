# In[1]: 
import json

with open("full.json") as f:
    data = json.load(f)

# In[2]: 
with open("charset.txt", "w") as f:
    f.write("\n".join(sorted(data.keys())))

# In[3]: 
with open("charset.txt", "w") as f_charset, \
     open("wordset.txt", "w") as f_wordset:
    keys = [(len(key), key) for key in data.keys()]
    keys.sort()
    charkeys, wordkeys = [], []
    for l, c in keys:
        if l == 1:
            charkeys.append(c)
        else:
            wordkeys.append(c)
    f_charset.write("\n".join(charkeys))
    f_wordset.write("\n".join(wordkeys))
