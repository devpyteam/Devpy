from bs4 import BeautifulSoup
import urllib.request
import datetime
import re

# 출력 파일 명
t = datetime.date.today()
OUTPUT_FILE_NAME = "france_test" + t.strftime("%y-%m-%d") + ".txt"
# 긁어 올 URL
URL = 'http://lexpansion.lexpress.fr/actualite-economique/hausse-de-la-csg-le-maire-demande-aux-retraites-un-effort-pour-les-jeunes_1936553.html'
URL2 = 'http://lexpansion.lexpress.fr/actualite-economique/budget-pourquoi-le-gouvernement-veut-surtaxer-les-grandes-entreprises_1935813.html'
URL3 = 'http://lexpansion.lexpress.fr/actualite-economique/fruits-et-legumes-1-50-8364-le-kilo-de-tomates-le-juste-prix-pour-le-producteur_1935921.html'
URL4 =  'http://lexpansion.lexpress.fr/actualite-economique/le-taux-de-chomage-a-baisse-de-0-1-point-au-second-trimestre_1935772.html'
URL5 =  'http://lexpansion.lexpress.fr/actualite-economique/comment-facebook-est-revenu-en-chine-par-la-petite-app_1934915.html'


# 크롤링 함수
def get_text(URL):
    url = urllib.request.urlopen(URL)
    soup = BeautifulSoup(url,'html.parser')
    text = ''
    p = soup.select("#page > article > div > div.article_full_container > div.article_container > p")
    for li in p:
        text = text + str(li.text)
    comment = soup.select("#comments_item > div > p.comment_text")
    for li in comment:
        text = text + str(li.text)
    return text

def get_text2(URL2):
    url = urllib.request.urlopen(URL2)
    soup = BeautifulSoup(url,'html.parser')
    text = ''
    p = soup.select("#page > article > div > div.article_full_container > div.article_container > p")
    for li in p:
        text = text + str(li.text)
    return text

def get_text3(URL3):
    url = urllib.request.urlopen(URL3)
    soup = BeautifulSoup(url,'html.parser')
    text = ''
    p = soup.select("#page > article > div > div.article_full_container > div.article_container > p")
    for li in p:
        text = text + str(li.text)
    return text

def get_text4(URL4):
    url = urllib.request.urlopen(URL4)
    soup = BeautifulSoup(url,'html.parser')
    text = ''
    p = soup.select("#page > article > div > div.article_full_container > div.article_container > p")
    for li in p:
        text = text + str(li.text)
    print(text)
    return text

def get_text5(URL5):
    url = urllib.request.urlopen(URL5)
    soup = BeautifulSoup(url,'html.parser')
    text = ''
    p = soup.select("#page > article > div > div.article_full_container > div.article_container > p")
    for li in p:
        text = text + str(li.text)
    return text


# 클리닝 함수
def clean_text(text):
    cleaned_text = re.sub('[0-9]', '', text)
    cleaned_text = re.sub('[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"]',
                          '', cleaned_text)
    return cleaned_text

# 메인 함수
def main():
    open_output_file = open(OUTPUT_FILE_NAME, 'w', encoding='UTF-8', newline='')
    result_text = get_text(URL) + "\n" +get_text2(URL2)\
                  + "\n" +get_text3(URL3)\
                  + "\n" +get_text4(URL4)\
                  + "\n" +get_text5(URL5)
    result_text = clean_text(result_text)
    open_output_file.write(result_text)
    open_output_file.close()


if __name__ == '__main__':
    main()
