from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import flask_login
import pymysql

app = Flask(__name__)

app.secret_key = 'super secret string'  # Change this!

conn = pymysql.connect(
        host= 'database-2.cjv1pfdwijy3.us-east-2.rds.amazonaws.com', 
        port = 3306,
        user = 'admin', 
        password = 'ezbreezy',
        db = 'mydb',
        )

# insert query
def insert_details(name,password,email):
    cur=conn.cursor()
    cur.execute("INSERT INTO UserInfo (UserID,Password,Email) VALUES (%s,%s,%s)", (name,password,email))
    conn.commit()
#read the data
def get_details():
    cur=conn.cursor()
    cur.execute("SELECT *  FROM UserInfo")
    details = cur.fetchall()
    return details

# login_manager = flask_login.LoginManager()

# login_manager.init_app(app)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/about.html', methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/causes.html', methods=['GET'])
def causes():
    return render_template('causes.html')

@app.route('/login.html', methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/login.html', methods=['POST'])
def authLogin():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
    return render_template('index.html')

@app.route('/contact.html', methods=['GET'])
def contact():
    return render_template('contact.html')

@app.route('/single.html', methods=['GET'])
def single():
    return render_template('single.html')

@app.route('/form.html', methods=['GET'])
def form():
    return render_template('form.html')

@app.route('/Sign-up.html', methods=['GET'])
def Signup():
    return render_template('Sign-up.html')

@app.route('/insert', methods=['POST'])
def makeuser():
    if request.method == 'POST':
        UserID = request.form.get('username'),
        Password = request.form.get('password'),
        Email = request.form.get('email')
        insert_details(UserID,Password,Email)
        return render_template("index.html")

class User(flask_login.UserMixin):
    pass

# @login_manager.user_loader
# def user_loader(email):
#     if email not in users:
#         return

#     user = User()
#     user.id = email
#     return user


# @login_manager.request_loader
# def request_loader(request):
#     email = request.form.get('email')
#     if email not in users:
#         return

#     user = User()
#     user.id = email
#     return user
