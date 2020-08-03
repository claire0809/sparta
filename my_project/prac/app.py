from flask import Flask, render_template, jsonify, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/home/hello')
def home():
    return 'Hello home! hello!'

#
# ## HTML을 주는 부분
# @app.route('/')
# def home():
#     return render_template('index.html')


## API 역할을 하는 부분
@app.route('/test', methods=['GET'])
def test_get():
    title_receive = request.args.get('title_give')
    print(title_receive)
    return jsonify({'result': 'success', 'msg': '이 요청은 GET!'})

# post 방식. 위에는 get 방식.
@app.route('/test', methods=['POST'])
def test_post():
    title_receive = request.form['title_give']
    print(title_receive)
    return jsonify({'result': 'success', 'msg': '이 요청은 POST!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)


