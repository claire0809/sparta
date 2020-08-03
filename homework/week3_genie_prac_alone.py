import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200713', headers=headers)
# **질문: json()은 필요 없는 과정인지?? requests의 정확한 개념?
# genie_music = data.json()

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')
# print(soup)

# select를 이용해서, tr들을 불러오기
# movies = soup.select('#old_content > table > tbody > tr')

# !주의! : select , select_one 구분 잘 할 것
# ssak_three = soup.select_one('#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis')
# print(ssak_three)

trs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')
# print(trs)

for tr in trs:
    # print(tr)
    title = tr.select_one('td.info > a.title.ellipsis').text.strip()
    # !주의!:33라인. select_one 써야함. for문으로 배열 반복하면서 select_one으로 값 꺼내서 반복.
    # !주의!:33라인. ('td.info > a.title.ellipsis')복사할 때, td.info 앞에 # 붙이면 안됨. id로 인식하기 때문에 print(title) = none으로 나옴
    singer = tr.select_one('td.info > a.artist.ellipsis').text
    rank = tr.select_one('td.number').text[0:2].strip()
    # !주의!: 윗라인. 파이썬 문자열 자르기. 검색하면서 풀기.
    print(rank,title,singer)
    doc = {
        'rank': rank,
        'title': title,
        'singer': singer
    }

    db.genie.insert_one(doc)

#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis

#body-content > div.newest-list > div > table > tbody > tr:nth-child(2) > td.info > a.title.ellipsis

#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number

#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.artist.ellipsis