import matplotlib.pyplot as plt
import pandas as pd
import csv
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

data = load_files("./test_data/*.txt")
print(data)
train_data = data['freqs']

with open("./test.csv", "w", encoding="utf-8", newline = '') as fp:
    thedatawriter = csv.writer(fp)
    for row in train_data:
        thedatawriter.writerow(row)

