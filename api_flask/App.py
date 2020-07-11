from flask import Flask, jsonify, make_response
from flask import request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSLQ_HOST'] = 'localhost'
app.config['MYSLQ_USER'] = 'root'
app.config['MYSLQ_PASSWORD'] = 'password'
app.config['MYSLQ_DB'] = 'akuro'

mysql = MySQL(app)

@app.route('/procesingEndpoint', methods=['POST'])
def procesing_data():
    if(request.method) == 'POST':
        data = request.get_json()
        amount = data["amount"]
        id = data["id"]
        data = {'success': 'ok', 'total': (amount*id)/4}
        return make_response(jsonify(data), 201)
    else:
        data = {'error'}
        return make_response(jsonify(data), 400)


if __name__ == '__main__':
    app.run(port =3000, debug = True)

