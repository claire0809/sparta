# from flask import Flask, render_template, jsonify, request
# import requests
# from bs4 import BeautifulSoup
# from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

# app = Flask(__name__)
#
# client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
# db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만들거나 사용합니다.
#
#
# @app.route('/')
# def home():
#     return render_template('index.html')
#
#
# @app.route('/memo', methods=['POST'])
# def post_article():
#     # 1. 클라이언트로부터 데이터를 받기
#     url = request.form['url']
#     comment = request.form['comment']
#     print(url, comment)
#
#     # 2. meta tag를 스크래핑하기
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
#     data = requests.get(url, headers=headers)
#
#     soup = BeautifulSoup(data.text, 'html.parser')
#     # print(soup)
#     # css selector copy가 안되서 직접 입력함 or 수업자료 확인 & 따옴표를 겉에는 작은따옴표, property는 쌍따옴표로 하거나,,, 쌍따옴표로 둘 다 하려면 \\백슬래쉬 를 사용해야함.
#     # title = soup.select_one('meta[property="og:title"]') 뒤에 ['content'] 붙이면 그린북 글자만.
#     title = soup.select_one('meta[property="og:title"]')['content']
#     desc = soup.select_one('meta[property="og:description"]')['content']
#     image = soup.select_one('meta[property="og:image"]')['content']
#     print(title, desc, image)
#
#     # 3. mongoDB에 데이터 넣기
#     doc = {
#         'title': title,
#         'desc': desc,
#         'image': image,
#         'comment': comment,
#         'url': url
#     }
#
#     db.articles.insert_one(doc)
#
#     return jsonify({'result': 'success', 'msg': 'POST 연결되었습니다!'})
#
#
# @app.route('/memo', methods=['GET'])
# def read_articles():
#     # 1. mongoDB에서 _id 값을 제외한 모든 데이터 조회해오기(Read) (_id값을 제외하지 않으면 jsonify로 읽어올 때 error생김)
#     # collection aritcles와 변수 aritlces는 전혀 다른 내용. 관계 없음 & cursor라는 것 대신에 list로 감싸줘서 모든 정보를 가져옴
#     articles = list(db.articles.find({}, {'_id': False}))
#     print(articles)
#
#     # 2. articles라는 키 값으로 articles 정보 보내주기
#     return jsonify({'result': 'success', 'msg': articles})
#
#
# if __name__ == '__main__':
#     app.run('0.0.0.0', port=5000, debug=True)







# ***### prac_alone###***
#
# from flask import Flask, render_template, jsonify, request
# import requests
# from bs4 import BeautifulSoup
# from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
#
# app = Flask(__name__)
#
# client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
# db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만들거나 사용합니다.
#
#
# @app.route('/')
# def home():
#     return render_template('index.html')
#
#
# @app.route('/memo', methods=['POST'])
# def post_article():
#     # 1. 클라이언트로부터 데이터를 받기
#     url_receive = request.form['url_give']
#     comment_receive = request.form['comment_give']
#
#     # **질문: print했을 때 왜 error나는지..?? emptry response 내용의 에러. (localhost:5000에서 아티클url input과 간단 코멘트 input에 입력하고, 기사저장했을 때 콘솔창에서 에러 뜸)
#     # **질문: print된 내용을 확인하는 곳?? 어디서 확인?
#     # print(url_receive, comment_receive)
#
#     # 2. meta tag를 스크래핑하기
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
#     data = requests.get(url_receive, headers=headers)
#     soup = BeautifulSoup(data.text, 'html.parser')
#     # **질문: print(soup)내용은 어디서 확인하는지?
#     print(soup)
#
#     og_image = soup.select_one('meta[property="og:image"]')['content']
#     og_title = soup.select_one('meta[property="og:title"]')['content']
#     og_description = soup.select_one('meta[property="og:description"]')['content']
#     # **질문 : print 확인하는 곳?
#     # print(og_image, og_title, og_description)
#
#
#     # 3. mongoDB에 데이터 넣기
#     doc = {
#         'url': url_receive,
#         'title': og_title,
#         'desc': og_description,
#         'image': og_image,
#         'comment': comment_receive
#     }
#
#     db.aaarticles.insert_one(doc)
#     return jsonify({'result': 'success', 'msg': 'POST 연결되었습니다!'})
#
#
# @app.route('/memo', methods=['GET'])
# def read_articles():
#     # 1. mongoDB에서 _id 값을 제외한 모든 데이터 조회해오기(Read)
#     # 2. articles라는 키 값으로 articles 정보 보내주기
#     return jsonify({'result': 'success', 'msg': 'GET 연결되었습니다!'})
#
#
# if __name__ == '__main__':
#     app.run('0.0.0.0', port=5000, debug=True)



# ***### prac_alone2###***
from flask import Flask, render_template, jsonify, request
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

app = Flask(__name__)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만들거나 사용합니다.


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/memo', methods=['POST'])
def post_article():
    # 1. 클라이언트로부터 데이터를 받기 ('url_give') 라는 이름으로 찾겠다는 것.
    url_receive = request.form['url_give']
    comment_receive = request.form['comment_give']

    # 2. meta tag를 스크래핑하기

    # 타겟 URL을 읽어서 HTML를 받아오고,
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get('https://movie.naver.com/movie/bi/mi/basic.nhn?code=171539', headers=headers)

    # HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
    # soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
    soup = BeautifulSoup(data.text, 'html.parser')
    # print(soup)

    title = soup.select_one('meta[property="og:title"]')['content']
    image = soup.select_one('meta[property="og:image"]')['content']
    desc = soup.select_one('meta[property="og:description"]')['content']
    # print(title, image, desc)

    doc ={
        'title' : title,
        'image' : image,
        'desc' :desc,
        'url' : url_receive,
        'comment' : comment_receive
    }
    db.aaarticles.insert_one(doc)

    # 3. mongoDB에 데이터 넣기
    return jsonify({'result': 'success', 'msg': '저장이 완료되었습니다!'})


@app.route('/memo', methods=['GET'])
def read_articles():
    # 1. mongoDB에서 _id 값을 제외한 모든 데이터 조회해오기(Read)
    result = list(db.aaarticles.find({}, {'_id' : False}))
    print(result)
    # 2. articles라는 키 값으로 articles 정보 보내주기
    return jsonify({'result': 'success', 'msg': result})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
