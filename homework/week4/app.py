from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbhomework


## HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('index.html')


# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
    # 여길 채워나가세요!
    # 1. 클라이언트가 준 주문자이름, 수량, 주소, 전화번호 가져오기.
    name_receive = request.form['name_give']
    count_receive = request.form['count_give']
    address_receive = request.form['address_give']
    phone_receive = request.form['phone_give']
    # ***질문 : 아래줄. print 값이 error 인 이유? KeyError: 'name'   (name_give 데이터 입력하기 전이어서?)
    # 답 : 서버 먼저 만들면서 아직 name_give 값이 설정이 안되었기 때문.
    # 예를 들어 phone_receive2 = request.form['phone_give2'] 를 입력하고,save한 뒤 실행해도(?) 값이 없기 때문에 KeyError가 뜸.


    print(name_receive)
    print(count_receive)

    # # 2. DB에 정보 삽입하기
    doc = {
        'name': name_receive,
        'count': count_receive,
        'address': address_receive,
        'phone': phone_receive
    }

    db.orders.insert_one(doc)

    # # 3. 성공 여부 & 성공 메시지 반환하기
    return jsonify({'result': 'success', 'msg': '이 요청은 POST!! 주문완료!'})


# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
    # 여길 채워나가세요!
    order_list = list(db.orders.find({}, {'_id': False}))
    # print(order_list)

    return jsonify({'result': 'success', 'orders': order_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
