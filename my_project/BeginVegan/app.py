from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

client = MongoClient('mongodb://test:test@15.164.231.203', 27017)
db = client.dbsparta


# HTML 화면 보여주기
@app.route('/')
def home():
    return render_template('index2.html')


# API 역할을 하는 부분
@app.route('/api/mangoplate', methods=['GET'])
def show_mangoplate():
    # 1. db에서 mystar 목록 전체를 검색합니다. ID는 제외하고 like 가 많은 순으로 정렬합니다.
    mangoplate = list(db.mangoplate.find({}, {'_id': False}).skip(2).limit(3))
    print(mangoplate)

    return jsonify({'result': 'success', 'mangoplate': mangoplate})


@app.route('/api/hellonature', methods=['GET'])
def show_hellonature():
    # 1. db에서 mystar 목록 전체를 검색합니다. ID는 제외하고 like 가 많은 순으로 정렬합니다.
    hellonature = list(db.hellonature.find({}, {'_id': False}).skip(6).limit(5))
    print(hellonature)

    return jsonify({'result': 'success', 'hellonature': hellonature})



# @app.route('/api/like', methods=['POST'])
# def like_star():
#     # 1. 클라이언트가 전달한 name_give를 name_receive 변수에 넣습니다.
#     # 2. mystar 목록에서 find_one으로 name이 name_receive와 일치하는 star를 찾습니다.
#     # 3. star의 like 에 1을 더해준 new_like 변수를 만듭니다.
#     # 4. mystar 목록에서 name이 name_receive인 문서의 like 를 new_like로 변경합니다.
#     # 참고: '$set' 활용하기!
#     # 5. 성공하면 success 메시지를 반환합니다.
#     return jsonify({'result': 'success', 'msg': 'like 연결되었습니다!'})


# @app.route('/api/delete', methods=['POST'])
# def delete_star():
#     # 1. 클라이언트가 전달한 name_give를 name_receive 변수에 넣습니다.
#     # 2. mystar 목록에서 delete_one으로 name이 name_receive와 일치하는 star를 제거합니다.
#     # 3. 성공하면 success 메시지를 반환합니다.
#     return jsonify({'result': 'success', 'msg': 'delete 연결되었습니다!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)