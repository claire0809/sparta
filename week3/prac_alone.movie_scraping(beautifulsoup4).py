import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200716',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')

# title = soup.select_one("#old_content > table > tbody > tr:nth-child(2) > td.title > div > a")
#
# print(title)
# print(title.text)
# print(title["href"])

trs = soup.select("#old_content > table > tbody > tr")
# print(trs)
# id는 html문서에 하나밖에 없기 때문에, head, body로 들어오지 않고 바로 #old_content로 selector가 똑똑하게 복사된 것.

for tr in trs:
    # print(tr)
    title = tr.select_one("td.title > div > a")
    if title is not None:
        rank = tr.select_one("td:nth-child(1) > img")
        star = tr.select_one("td.point")

        print(rank["alt"], title.text, star.text)
        # * rank = .....["alt]  변수 자체에 붙여도 됨. star = ... .text 처럼 변수 자체에 붙여도 됨.


        # print(title.text)



# **질문1: rank가 if 문 바깥에 있는 경우는 안되는지?
# **질문2: print(rank)도 None이 있는데, 왜 if title is not None 처럼 title에만 조건을 다는지?
#  title = tr.select_one("td.title > div > a")
#  rank = tr.select_one("td:nth-child(1) > img")
#     if title is not None:
#       elif rank is not None:
#         print(title.text, rank["alt"])





