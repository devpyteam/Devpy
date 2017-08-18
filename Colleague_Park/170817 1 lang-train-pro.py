
from sklearn import svm, metrics
import glob, os.path ,re, json

files=glob.glob("./lang/train/*.txt")
train_data=[]
train_label=[]
for file_name in files :
    basename=os.path.basename(file_name)
    lang=basename.split("-")[0]
    file=open(file_name,"r",encoding="utf-8")
    text=file.read()
    text=text.lower()
    file.close()
    code_a = ord("a")
    code_z = ord("z")
    count = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for character in text:
        code_current=ord(character)
        if code_a<=code_current <=code_z :
            count[code_current-code_a] +=1
    total=sum(count)
    count=list(map(lambda n : n/total,count))
#리스트에 넣기
    train_label.append(lang)
    train_data.append(count)

files=glob.glob("./lang/test/*.txt")
test_data=[]
test_label=[]
for file_name in files :
    basename=os.path.basename(file_name)
    lang=basename.split("-")[0]
    file=open(file_name,"r",encoding="utf-8")
    text=file.read()
    text=text.lower()
    file.close()
    code_a = ord("a")
    code_z = ord("z")
    count = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for character in text:
        code_current=ord(character)
        if code_a<=code_current <=code_z :
            count[code_current-code_a] +=1
    total=sum(count)
    count=list(map(lambda n : round(n/total,3),count))
#리스트에 넣기
    test_label.append(lang)
    test_data.append(count)

clf = svm.SVC()
clf.fit(train_data, train_label)
predict=clf.predict(test_data)
score=metrics.accuracy_score(test_label, predict)
print("score=",score)
print("=========================================================================")
print("test_data=",test_data)
print("predict=",predict)

