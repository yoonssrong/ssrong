
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from flaskext.mysql import MySQL


app = Flask(__name__)

# MySQL 연결
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'yoonssrong'
app.config['MYSQL_DATABASE_PASSWORD'] = '1q2w3e4r!'
app.config['MYSQL_DATABASE_DB'] = 'yoonssrong$foodcal'
app.config['MYSQL_DATABASE_HOST'] = 'yoonssrong.mysql.pythonanywhere-services.com'
mysql.init_app(app)



@app.route('/')
def hello_world():
    return 'Hello from Flask!'

@app.route('/안녕')
def hello_world2():
    return 'Hello2 from Flask!'

@app.route('/hello')
def hello_world3():
    hello = 'Hello3 from Flask!'
    return hello

@app.route('/getdata')
def get():
    conn = mysql.connect()
    cursor = conn.cursor()
    sql = "SELECT * FROM foodcal;"
    cursor.execute(sql)
    data = cursor.fetchall()

    return data[0][2]

@app.route('/banana')
def banana():
    conn = mysql.connect()
    cursor = conn.cursor()
    sql = "SELECT * FROM foodcal;"
    cursor.execute(sql)
    data = cursor.fetchall()

    return data[0][2]



