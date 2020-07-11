from flask import Flask, jsonify, make_response
from flask import request
from flask_mysqldb import MySQL
from flask_cors import CORS

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'akuro'

CORS(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
mysql = MySQL(app)

@app.route('/procesingEndpoint', methods=['POST'])
def procesing_data():
    if(request.method) == 'POST':
        data = request.get_json()
        amount = data["amount"]
        id = data["id"]
        data = {'success': 'ok', 'total': (amount*id)/4}
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO transanction values(%s, %s)', (id, amount))
        mysql.connection.commit()
        return make_response(jsonify(data), 201)
    else:
        data = {'error'}
        return make_response(jsonify(data), 400)


if __name__ == '__main__':
    app.run(port =3000, debug = True)

