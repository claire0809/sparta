# import requests
# from bs4 import BeautifulSoup
#
# url = 'https://platum.kr/archives/120958'
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# data = requests.get(url, headers=headers)
#
# soup = BeautifulSoup(data.text, 'html.parser')
#
# # 여기에 코딩을 해서 meta tag를 먼저 가져와보겠습니다.
#
# og_image = soup.select_one('meta[property="og:image"]')
# og_title = soup.select_one('meta[property="og:title"]')
# og_description = soup.select_one('meta[property="og:description"]')
#
# print(og_image)
# print(og_title)
# print(og_description)
#
# url_image = og_image['content']
# url_title = og_title['content']
# url_description = og_description['content']
#
# print(url_image)
# print(url_title)
# print(url_description)

import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/bi/mi/basic.nhn?code=171539', headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')

#############################
# (입맛에 맞게 코딩)
#############################

# print(soup)

title = soup.select_one('meta[property="og:title"]')['content']
image = soup.select_one('meta[property="og:image"]')['content']
desc = soup.select_one('meta[property="og:description"]')['content']
print(title,image,desc)