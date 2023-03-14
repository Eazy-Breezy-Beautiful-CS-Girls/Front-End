from flask import Flask, render_template, request, redirect, url_for, flash, session, g
from flask_sqlalchemy import SQLAlchemy
import flask_login
import database


app = Flask(__name__)

app.secret_key = 'super secret string'  # Change this!

login_manager = flask_login.LoginManager()
login_manager.init_app(app)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/causes', methods=['GET'])
def causes():
    return render_template('causes.html')

@app.route('/Fundraiser-2', methods=['GET'])
def Fundraiser2():
    return render_template('Fundrasier-2.html')

@app.route('/Fundraiser-3', methods=['GET'])
def Fundraiser3():
    return render_template('Fundrasier-3.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if not len(database.get_details(username, password)) == 0:
            user = User()
            user.id = username
            user.password = password
            flask_login.login_user(user)
            database.add_login(username)
            flash('Logged in successfully.')
            session['user_id'] = username
            g.user = True
            return redirect(url_for('index'))
        return render_template('login.html')

@app.route('/contact', methods=['GET'])
def contact():
    return render_template('contact.html')

@app.route('/single', methods=['GET'])
def single():
    return render_template('single.html')

@app.route('/form', methods=['GET'])
def form():
    return render_template('form.html')

@app.route('/Sign-up', methods=['GET','POST'])
def Signup():
    if request.method == 'GET':
        return render_template('Sign-up.html')
    elif request.method == 'POST':
        UserID = request.form.get('username'),
        Password = request.form.get('password'),
        Email = request.form.get('email')
        database.insert_details(UserID,Password,Email)
        return login()

@app.route('/logout', methods=['GET'])
def logout():
    flask_login.logout_user()
    return redirect(url_for('index'))

# @app.before_request
# def load_logged_in_user():
#     """If a user id is stored in the session, load the user object from
#     the database into ``g.user``."""
#     user_id = session.get("user_id")

#     if user_id is None:
#         g.user = None
#     else:
#         g.user = (
#             database.get_login(user_id)
#         )

class User(flask_login.UserMixin):
    pass

@login_manager.user_loader
def user_loader(id):
    if len(database.get_login(id)) ==0 :
        return

    user = User()
    user.id = id
    return user
