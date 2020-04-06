from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('127.0.0.1', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbhomework                     # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/checkorder')
def show_table():
    return render_template('checkoder.html')


## API 역할을 하는 부분
@app.route('/oderlist', methods=['POST'])
def make_order():
    user_name = request.form['ClientName']
    oder_amount = request.form['exampleFormControlSelect1']
    user_address = request.form['ClientAddr']
    user_callnumber = request.form['ClientTel']

    oder_list = {
        'user_name' : user_name,
        'oder_amount' : oder_amount,
        'user_address' : user_address,
        'user_callnumber': user_callnumber
            }
    db.dbhomework.insert_one(oder_list)
    return jsonify({'result':'success', 'msg': '주문이 성공적으로 이루어졌습니다'})


@app.route('/oderlist', methods=['GET'])
def read_order():
    oderfromUser = list(db.dbhomework.find({},{'_id':0}))
    return jsonify({'result': 'success', 'oder': oderfromUser})


if __name__ == '__main__':
    app.run('127.0.0.1', port=5000, debug=True)