from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse
from flaskext.mysql import MySQL
import json
import simplejson
import pymysql


app = Flask(__name__)
api = Api(app)


# MySQL 연결
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '910425'
app.config['MYSQL_DATABASE_DB'] = 'univ'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


@app.route("/")
def hello():
    return "Hello flask!"


class GetData(Resource):
    def get(self):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()

            sql = "SELECT student.ID FROM student;"

            cursor.execute(sql)

            data = cursor.fetchall()

            return data[0][0]

        except Exception as e:
            return {'error': str(e)}


class CreateUser(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('email', type=str)
            parser.add_argument('user_name', type=str)
            parser.add_argument('password', type=str)
            args = parser.parse_args()

            _userEmail = args['email']
            _userName = args['user_name']
            _userPassword = args['password']

            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('sp_create_user', (_userEmail, _userName, _userPassword))
            data = cursor.fetchall()

            if len(data) is 0:
                conn.commit()
                return {'StaatusCode': '200', 'Message': 'User creation success'}
            else:
                return {'StatusCode': '1000', 'Message': str(data[0])}

        except Exception as e:
            return {'error': str(e)}



class RegistUser1(Resource):
    def post(self):
        return {'result': 'ok'}

class RegistUser2(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str)
        parser.add_argument('email', type=str)
        args = parser.parse_args()

        name = args['name']
        email = args['email']

        return {'name': name, 'email': email}


api.add_resource(GetData, '/getdata')
api.add_resource(CreateUser, '/user')
api.add_resource(RegistUser1, '/adduser1/add1')
api.add_resource(RegistUser2, '/adduser2')



# if __name__ == '__main__':
#     app.run(debug=True)
