import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200716',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨. BeautifulSoup를 이용해서 파이썬이 알아들을 수 있는 구조로 바꾼 뒤 soup 에 담은 것
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')

# 데이터이름.text : html 내용을 text로 가져오는 것.
# 데이터이름["속성이름"] : 속성을 가져오는 것
# 그린북: element 로 들어가서 마우스 오른쪽: copy 에서 css selector 를 복사함.
# .select_one : css의 한 요소를 선택하는 것(?) .select_one에 복사한 selector 내용을 붙여넣기.

# name = soup.select_one("#old_content > table > tbody > tr:nth-child(2) > td.title > div > a")
# print(name.text)
# tr:nth-child(2)인 것은 두 번째 <tr>에서 css selector를 복사했기 때문. 기존 <tr>에서 새로 추가된 부분은 td.title > div > a 이 부분임.

tr_list = soup.select("#old_content > table > tbody > tr")
for tr in tr_list:
    title = tr.select_one("td.title > div > a")
    #  td.title : tag가 td이면서 class가 title인 것.

    rank_image = tr.select_one("td:nth-child(1) > img")
#    rank_image 변수에서 select_one 할 때,, .ac image?? (클래스가 .ac <<다시찾아보기)
#     #old_content > table > tbody > tr:nth-child(2)
    point_tag = tr.select_one("td.point")
    if title is not None:
        name = title.text
        rank = rank_image["alt"]
        point = point_tag.text
        print(rank, name, point)

