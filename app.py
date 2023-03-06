from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
#import flask_login

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:ezbreezy@database-2.cjv1pfdwijy3.us-east-2.rds.amazonaws.com:3306/database-2'
db = SQLAlchemy(app)

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

@app.route('/Sign-up.html', methods=['GET','POST'])
def MakeUser():
    if request.method == 'POST':
        user = User(
            UserID = request.form.get('username'),
            Password = request.form.get('password'),
            Email = request.form.get('email')
        )
        
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("index.html"))
        
    return render_template('Sign-up.html')

class User(flask_login.UserMixin):
    
    def __init__(self, UserID, Password, Email):
        self.UserID = UserID
        self.Email = Email
        self.Password = Password


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
