import urllib.request
from bs4 import BeautifulSoup
import time
from sklearn import svm, metrics
import glob, os.path ,re, json

# train data
# HTML 가져오기
url = "http://www.zeit.de/index"
response = urllib.request.urlopen(url)
# HTML 분석하기
soup = BeautifulSoup(response, "html.parser")
# 원하는 데이터 추출하기 --- (※1)
results = soup.select("#main > div > div.cp-area.cp-area--major  div > h2 > a")
i=0
for result in results:
  i=i+1
  print(i,"st article")
  print("title:" , result.attrs["title"])
  url_article=result.attrs["href"]
  response = urllib.request.urlopen(url_article)
  soup_article=BeautifulSoup(response, "html.parser")
  content=soup_article.select_one("p")

  output=""
  for item in content.contents:
    stripped=str(item).strip()
    if stripped == "":
      continue
    if stripped[0] not in ["<","/"]:
      output+=str(item).strip()
      print(output)

# 추출한 data를 txt 화일로 저장하기
  fn= "de" +"--"+ str(i)+ ".txt"
  fw = open(fn, 'w', encoding='UTF-8', newline='')
 # f = open("C:/Python/새파일.txt", 'w')
  result_text = output
  fw.write(result_text)
  fw.close()
  # 1초휴식 : 초당 서버호츨 횟수가 늘어나면, 아이디 차단당할수 있음. 휴식시간이 필요함
  time.sleep(1.5)

# 학습시키기
files=glob.glob("*--*.txt")
train_data=[]
train_label=[]
i=0
for file_name in files :
    i=i+1
    print(i)
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
    total=sum(count)+0.00001
    count=list(map(lambda n : n/total,count))
#리스트에 넣기
    train_label.append(lang)
    train_data.append(count)


# 테스트 하기: 프랑스어 4개 화일(6~9번)을 테스용 데이터로 사용함
i=0
files=glob.glob("*---*.txt")
test_data=[]
test_label=[]
for file_name in files :
    i=i+1
    print(i)
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
    total=sum(count)+0.00001
    count=list(map(lambda n : round(n/total,3),count))
#리스트에 넣기
    test_label.append(lang)
    test_data.append(count)

# 평가하기
clf = svm.SVC()
clf.fit(train_data, train_label)
predict=clf.predict(test_data)
score=metrics.accuracy_score(test_label, predict)
print("score=",score)
print("=========================================================================")
print("test_data=",test_data)
print("predict=",predict)

