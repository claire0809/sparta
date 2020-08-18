# from flask import Flask, render_template, jsonify, request
# from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
#
# app = Flask(__name__)
#
# client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
# db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.
#
#
# ## HTML을 주는 부분
# @app.route('/')
# def home():
#     return render_template('index.html')
#
#
# ## API 역할을 하는 부분
# @app.route('/review', methods=['POST'])
# def write_review():
#     # 1. 클라이언트가 준 title, author, review 가져오기.
#     title_receive = request.form['title_give']
#     author_receive = request.form['author_give']
#     review_receive = request.form['review_give']
#
#     # 2. DB에 정보 삽입하기
#
#     review = {
#         'title': title_receive,
#         'author': author_receive,
#         'review': review_receive
#     }
#
#     db.reviews.insert_pne(review)
#     # 3. 성공 여부 & 성공 메시지 반환하기
#     return jsonify({'result': 'success', 'msg': '리뷰가 성공적으로 작성되었습니다!'})
#
#
# @app.route('/review', methods=['GET'])
# def read_reviews():
#     reviews = list(db.reviews.find({}, {'_id' : 0}))
#     return jsonify({'result': 'success', 'reviews': reviews})
#
#
# if __name__ == '__main__':
#     app.run('0.0.0.0', port=5000, debug=True)


#  ***처음부터 다시***

from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

app = Flask(__name__)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.


## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')


## API 역할을 하는 부분
@app.route('/review', methods=['POST'])
def write_review():
    # 1. 클라이언트가 준 title, author, review 가져오기.
    title_receive = request.form['title_give']
    author_receive = request.form['author_give']
    review_receive = request.form['review_give']
    # 2. DB에 정보 삽입하기(몽고DB에 저장하려면 doc 만들고 dictionary 형태로 저장)
    doc = {
        'title' : title_receive,
        'author' : author_receive,
        'review' : review_receive
    }
    db.bookreview.insert_one(doc)

    # 3. 성공 여부 & 성공 메시지 반환하기
    return jsonify({'result': 'success', 'msg': '잘 저장되었습니다'})

@app.route('/review', methods=['GET'])
def read_reviews():
    # db에서 값 불러와서 보이게 해줘야 함
    reviews = list(db.bookreview.find({}, {'_id': False}))
    # print(reviews)  :하고, localhost:5000 에서 제목, 작가, 리뷰 값 넣고, run창(?)에서 확인
    return jsonify({'result': 'success', 'all_reviews': reviews})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
