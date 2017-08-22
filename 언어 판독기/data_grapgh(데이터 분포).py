import matplotlib.pyplot as plt
import pandas as pd
import json
import glob , os.path, re, json

def check_freq(fname):
    name = os.path.basename(fname)
    lang = re.match(r'^[a-z]{2,}',name).group()
    with open(fname, "r", encoding="utf-8") as f:
        text = f.read()
    text = text.lower()

    cnt = [0 for n in range(0,26)]
    code_a = ord("a")
    code_z = ord("z")

    for ch in text:
        n = ord(ch)
        if code_a <= n <= code_z:
            cnt[n-code_a] +=1

    total = sum(cnt)
    freq = list(map(lambda n: n/ total, cnt))
    return(freq, lang)

def load_files(path):
    freqs = []
    labels = []
    file_list = glob.glob(path)
    for fname in file_list:
        r = check_freq(fname)
        freqs.append(r[0])
        labels.append(r[1])
    return {"freqs":freqs, "labels":labels}

data = load_files("../Colleague_Kang/france_test17-08-21.txt")

with open("./freq.json", "w", encoding="utf-8") as fp:
    json.dump([data], fp)

with open("./freq.json", "r", encoding="utf-8") as fp:
    freq = json.load(fp)

lang_dic = {}
for i, lbl in enumerate(freq[0]["labels"]):
    fq = freq[0]["freqs"][i]
    if not (lbl in lang_dic):
        lang_dic[lbl] = fq
        continue
    for idx, v in enumerate(fq):
        lang_dic[lbl][idx] = (lang_dic[lbl][idx] + v) / 2

asclist = [[chr(n) for n in range(97,97+26)]]
df = pd.DataFrame(lang_dic, index=asclist)

plt.style.use('ggplot')
df.plot(kind = "bar", subplots = True, ylim=(0,0.15))
plt.savefig("land-plot.png")