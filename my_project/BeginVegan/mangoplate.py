### 망고플레이트###
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('mongodb://test:test@15.164.231.203', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 사용합니다. 'dbsparta' db가 없다면 새로 만듭니다.

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.mangoplate.com/top_lists/721_vegan', headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')
# print(soup)

restaurants = soup.select('#contents_list > ul > li')
# print(restaurants)


for restaurant in restaurants:
    name = restaurant.select_one('div > figure > figcaption > div > span > a > h3').text
    location = restaurant.select_one('div > figure > figcaption > div > p').text
    image = restaurant.select_one('div > figure > a > div > img')['data-original']
    final_url = 'https://www.mangoplate.com/' + restaurant.select_one('div > figure > a')['href']
    print(final_url)
    # imaage:s plit??
    # print(image)

    doc = {
        'name': name,
        'location': location,
        'image': image,
        'final_url': final_url
    }
    db.mangoplate.insert_one(doc)

# *질문: <더보기> 페이지 이후의 크롤링 하는 방법?
