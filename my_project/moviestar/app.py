# from pymongo import MongoClient
#
# from flask import Flask, render_template, jsonify, request
#
# app = Flask(__name__)
#
# client = MongoClient('localhost', 27017)
# db = client.dbsparta
#
#
# # HTML 화면 보여주기
# @app.route('/')
# def home():
#     return render_template('index.html')
#
#
# # API 역할을 하는 부분
# @app.route('/api/list', methods=['GET'])
# def show_stars():
#     # 1. db에서 mystar 목록 전체를 검색합니다. ID는 제외하고 like 가 많은 순으로 정렬합니다.
#     stars = list(db.mystar.find({}, {'_id': False}).sort('like', -1))
#     # print(stars)
#
#     # 참고) find({},{'_id':False}), sort()를 활용하면 굿!
#     #  몽고db에서 가져올 때, sort하는 법. 가져온 뒤에 파이썬에서 sort 하는 법 두 가지 있음. (수업에서는 전자로 함)
#     #  참고용) "파이썬"에서 sort 하는 법(sort, sorted) : sorted(stars, key=lambda x: x['like'], reverse=True) 라고 적어야함.. 우리가 한 것 처럼pymongo에서 sort 하는 것 추천.
#     #  pymongo sort 내용 구글링 해보기. mydb["customers"] 가 db.mystar임.
#     #  -1 은 내림차순. 1은 오름차순.
#     # 2. 성공하면 success 메시지와 함께 stars_list 목록을 클라이언트에 전달합니다.
#     return jsonify({'result': 'success', 'stars_list': stars})
#
#
# @app.route('/api/like', methods=['POST'])
# def like_star():
#     # 1. 클라이언트가 전달한 name_give를 name_receive 변수에 넣습니다.
#     name_receive = request.form['name_give']
#     # print('like', name_receive) localhost:5000에서 '위로' 누른 후, run창에서 확인
#
#     # 2. mystar 목록에서 find_one으로 name이 name_receive와 일치하는 star를 찾습니다.
#     star = db.mystar.find_one({'name': name_receive})
#     # print(star) localhost:5000에서 '위로' 누른 후, run창에서 확인
#
#     # 3. star의 like 에 1을 더해준 new_like 변수를 만듭니다.
#     new_like = star['like'] + 1
#
#     # 4. mystar 목록에서 name이 name_receive인 문서의 like 를 new_like로 변경합니다.
#     # 참고: '$set' 활용하기!  (3주차 몽고db update 로직 다시 확인해보기)
#     db.mystar.update_one({'name': name_receive}, {'$set': {'like': new_like}})
#     # 여기까지 한 뒤, localhost:5000에서 위로! 누르고, 새로고침 해보기.
#     # index.html 파일에서 자동으로 새로고침 되도록 함수에 window.location.reload(); 추가.
#
#     # 5. 성공하면 success 메시지를 반환합니다.
#     return jsonify({'result': 'success', 'msg': 'like 연결되었습니다!'})
#
#
# @app.route('/api/delete', methods=['POST'])
# def delete_star():
#     # 1. 클라이언트가 전달한 name_give를 name_receive 변수에 넣습니다.
#     name_receive = request.form['name_give']
#     # print('like', name_receive) : localhost:5000에서 삭제 누른 후, run창에서 확인
#
#     # 2. mystar 목록에서 delete_one으로 name이 name_receive와 일치하는 star를 제거합니다.
#     db.mystar.delete_one({'name': name_receive})
#
#     # 3. 성공하면 success 메시지를 반환합니다.
#     return jsonify({'result': 'success', 'msg': 'delete 연결되었습니다!'})
#
#
# if __name__ == '__main__':
#     app.run('0.0.0.0', port=5000, debug=True)


# practice alone

from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta


# HTML 화면 보여주기
@app.route('/')
def home():
    return render_template('index2.html')


# API 역할을 하는 부분
# ***질문: 왜 다른 bookreview나 alonememo처럼 post 방식 먼저 만들지 않고, get 방식부터 먼저 만드는지??(이미 데이터 크롤링이 되어있어서?)

@app.route('/api/list', methods=['GET'])
def show_stars():
    # 1. db에서 mystar 목록 전체를 검색합니다. ID는 제외하고 like 가 많은 순으로 정렬합니다.
    # 참고) find({},{'_id':False}), sort()를 활용하면 굿!
    stars = list(db.mystar.find({}, {'_id': False}).sort("like", -1))
    # ***질문 : 97라인(윗라인)완성 후, 임의로 LIKE 수정했을 때, robo3T에서 데이터 순서 바뀌어야 하는 것 아닌지? 아니면,저장된 데이터 순서 그대로 있어야 하는 것?
    # ***질문 : localhost:5000/api/list 에서만 like 순위 반영해서 데이터 순서 바뀌어 나오는 것인지..?
    # 2. 성공하면 success 메시지와 함께 stars_list 목록을 클라이언트에 전달합니다.
    return jsonify({'result': 'success', 'stars_list': stars})


# *** 질문: bookreview나 alonememo에서 localhost:5000/뒷부분 이 같을 때, 왜 get 내용만 뜨는 것인지? post 내용은 어떻게 확인??
@app.route('/api/like', methods=['POST'])
def like_star():
    # 1. 클라이언트가 전달한 name_give를 name_receive 변수에 넣습니다.
    name_receive = request.form['name_give']

    # 2. mystar 목록에서 find_one으로 name이 name_receive와 일치하는 star를 찾습니다.
    star = db.mystar.find_one({'name': name_receive})
    print(star)

    # 3. star의 like 에 1을 더해준 new_like 변수를 만듭니다.
    new_like = star['like'] + 1

    # 4. mystar 목록에서 name이 name_receive인 문서의 like 를 new_like로 변경합니다.
    # 참고: '$set' 활용하기!
    db.mystar.update_one({'name': name_receive}, {'$set': {'like': new_like}})

    # 5. 성공하면 success 메시지를 반환합니다.
    return jsonify({'result': 'success', 'msg': 'like 연결되었습니다!'})


@app.route('/api/delete', methods=['POST'])
def delete_star():
    # 1. 클라이언트가 전달한 name_give를 name_receive 변수에 넣습니다.
    name_receive = request.form['name_give']

    # 2. mystar 목록에서 delete_one으로 name이 name_receive와 일치하는 star를 제거합니다.
    # 3. 성공하면 success 메시지를 반환합니다.
    return jsonify({'result': 'success', 'msg': 'delete 연결되었습니다!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
