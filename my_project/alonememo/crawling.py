# 크롤링 파일을 따로 만든 이유: 실행된 코드만 따로 app.py에 붙이는 것이 더욱 효율적. (계속 css selector등을 확인하면서 진행해야 하기 때문에(?))

#  교재 20번-3 메타태그 스크래핑 한 것
import requests
from bs4 import BeautifulSoup

url = 'https://movie.naver.com/movie/bi/mi/basic.nhn?code=171539'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(url, headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')
# print(soup)
# css selector copy가 안되서 직접 입력함 or 수업자료 확인 & 따옴표를 겉에는 작은따옴표, property는 쌍따옴표로 하거나,,, 쌍따옴표로 둘 다 하려면 \\백슬래쉬 를 사용해야함.
# title = soup.select_one('meta[property="og:title"]') 뒤에 ['content'] 붙이면 그린북 글자만.
title = soup.select_one('meta[property="og:title"]')['content']
desc = soup.select_one('meta[property="og:description"]')['content']
image = soup.select_one('meta[property="og:image"]')['content']
print(title, desc , image)

# 여기까지 하면 크롤링(스크래핑) 끝. app.py 2번)meta tag를 스크래핑하기 에 붙여넣기 해야함.

