import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('mongodb://test:test@15.164.231.203', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 사용합니다. 'dbsparta' db가 없다면 새로 만듭니다.

driver = webdriver.Chrome("chromedriver.exe")
driver.get(
    "https://www.hellonature.co.kr/fdp002.do?goTo=moduleToDpList&gubunFlag=M&dataFlag=108&dataCd=&grpCd=&mainGrpCd=ALL&stamp=XLee")

# soup = BeautifulSoup(driver.page_source, 'html.parser')

# for문 주석 풀기(pagination 스크롤 해서 크롤링하는 것)
for i in range(22):
    driver.find_element_by_tag_name('body').send_keys(Keys.END)
    driver.implicitly_wait(10)
    time.sleep(5)
    # print(soup)
soup = BeautifulSoup(driver.page_source, 'html.parser')
lists = soup.select('#dpItemList > li')

for list in lists:
    a = list.select_one('div > div.thumb > a')['onclick']
    # print(a)
    # break
    image = list.select_one('div > div.thumb > a > div.img > img')['src']
    # print(image)
    name = list.select_one('div > div.info > div.name > a').text
    # print(name)
    # 질문: #dpItemList > li:nth-child(1) > div > div.info > div.cost    에 span 태그(?)추가. class 이름 추가. & text
    price = list.select_one('div > div.info > div.cost > span.after').text
    # print(price)
    url = list.select_one('div > div.thumb > a')['onclick']
    number = url.split("'")[1]
    final_url = "https://www.hellonature.co.kr/fdp001.do?goTo=dpItemView&itemCd=" + number + "&gubunFlag=M&ctgrCd=2020050005"
    # print(final_url)
    doc = {
        'image': image,
        'price': price,
        'name': name,
        'final_url': final_url
    }

    db.hellonature.insert_one(doc)

# https://www.hellonature.co.kr/fdp001.do?goTo=dpItemView&itemCd=028128&gubunFlag=M&ctgrCd=2020050005
# https://www.hellonature.co.kr/fdp001.do?goTo=dpItemView&itemCd=025976&gubunFlag=M&ctgrCd=2020050005

# dpItemList > li:nth-child(1) > div > div.thumb > a['onclick']
# dpItemList > li:nth-child(1) > div > div.thumb > a


# for i in range(22):
#     driver.find_element_by_tag_name('body').send_keys(Keys.END)
#     driver.implicitly_wait(10)
#     time.sleep(5)
#     lists = soup.select('#dpItemList > li')
#     for list in lists:
#         a = list.select_one('div > div.thumb > a')['onclick']
#         # print(a)
#         image = list.select_one('div > div.thumb > a > div.img > img')['src']
#         # print(image)
#         name = list.select_one('div > div.info > div.name > a').text
#         # print(name)
#         price = list.select_one('div > div.info > div.cost > span.after').text
#         # print(price)
#         url = list.select_one('div > div.thumb > a')['onclick']
#         number = url.split("'")[1]
#         final_url = "https://www.hellonature.co.kr/fdp001.do?goTo=dpItemView&itemCd=" + number + "&gubunFlag=M&ctgrCd=2020050005"
#         # print(final_url)
#         doc = {
#             'image': image,
#             'price': price,
#             'name': name,
#             'final_url': final_url
#         }
#         db.hellonature.insert_one(doc)
