import os
import functools

from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for
from base64 import b64encode
from FrontEnd.database import get_db

bp = Blueprint("auth", __name__, url_prefix="/auth")

def login_required(view):
    """View decorator that redirects anonymous users to the login page."""

    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for("auth.login"))

        return view(**kwargs)

    return wrapped_view

@bp.before_app_request
def load_logged_in_user():
    """If a user id is stored in the session, load the user object from
    the database into ``g.user``."""
    user_id = session.get("user_id")

    if user_id is None:
        g.user = None
    else:
        with get_db().cursor() as cursor:
            cursor.execute('SELECT UserID FROM LoggedIn WHERE UserID = %s', (user_id,))
            user = cursor.fetchone()
            g.user = (user)

@bp.route('/logout', methods=['GET'])
def logout():
    session.clear()
    get_db().cursor().execute('DELETE FROM LoggedIn WHERE UserID=%s', (g.user))
    get_db().commit()
    return redirect(url_for('index'))

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    username = request.form.get('username')
    password = request.form.get('password')
    if not get_db().cursor().execute("SELECT * FROM UserInfo WHERE UserID = %s AND Password = %s",(username, password)) == 0:
        get_db().cursor().execute("INSERT IGNORE INTO LoggedIn (UserID) VALUES (%s)",(username))
        get_db().commit()
        flash('Logged in successfully.')
        session.clear()
        session['user_id'] = username
        return redirect(url_for('index'))
    flash('Login Failed')
    return render_template('login.html')
    
@bp.route('/Sign-up', methods=['GET','POST'])
def Signup():
    if request.method == 'GET':
        return render_template('Sign-up.html')
    Fname = request.form.get('fname')
    Lname = request.form.get('lname')
    Email = request.form.get('email')
    UserID = request.form.get('username')
    Password = request.form.get('password')
    AuthPassword = request.form.get('auth_password')
    if Fname == '' or Lname == '':
        return render_template('Sign-up.html', no_name='Name Required')
    if UserID == '':
        return render_template('Sign-up.html', no_username='User ID Required')
    if Email == '':
        return render_template('Sign-up.html', no_email='Email Required')
    if Password == '':
        return render_template('Sign-up.html', no_password='Password Required')
    if Password!= AuthPassword:
        return render_template('Sign-up.html', no_match='Passwords must match')
    get_db().cursor().execute("INSERT IGNORE INTO UserInfo (UserID,Password,Email,FirstName,LastName) VALUES (%s,%s,%s,%s,%s)", (UserID,Password,Email,Fname,Lname))
    get_db().commit()
    return login()

@bp.route('/contact/<string:UserID>', methods=['GET','POST'])
@login_required
def contact(UserID):
    if request.method == 'GET':
        with get_db().cursor() as cursor:
            cursor.execute('SELECT * FROM UserInfo WHERE UserID = %s',(UserID))
            user = cursor.fetchone()
        try:
            image = b64encode(user[4]).decode('utf-8')
        except:
            image = None
        return render_template('contact.html', user=user, image=image)
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    email = request.form.get('email')
    bio = request.form.get('bio')
    get_db().cursor().execute('UPDATE IGNORE UserInfo SET FirstName = %s, LastName = %s, Email = %s, Bio = %s WHERE UserID = %s',(fname, lname, email, bio, UserID))
    get_db().commit()
    current_pass = request.form.get('c_pass')
    new_pass = request.form.get('n_pass')
    auth_pass = request.form.get('a_pass')
    if current_pass and new_pass:
        with get_db().cursor() as cursor:
            cursor.execute('SELECT Password FROM UserInfo WHERE UserID = %s',(UserID))
            user = cursor.fetchone()
            if current_pass == user[0]:
                if new_pass == auth_pass:
                    cursor.execute('UPDATE UserInfo SET Password = %s WHERE UserID = %s',(new_pass, UserID))
                    get_db().commit()
                elif new_pass != auth_pass:
                    flash('Passwords do not match')
            elif current_pass != user[0]:
                flash('Incorrect Password')
    with get_db().cursor() as cursor:
        cursor.execute('SELECT * FROM UserInfo WHERE UserID = %s',(UserID))
        user = cursor.fetchone()
        try:
            image = b64encode(user[4]).decode('utf-8')
        except:
            image = None
        return render_template('contact.html', user=user, image=image)

@bp.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      upload = request.files['pic']
      upload.save(upload.filename)
      with open(upload.filename, 'rb') as f:
        binaryData=f.read()
      get_db().cursor().execute('UPDATE UserInfo SET Pic = %s WHERE UserID = %s',(binaryData, g.user))
      get_db().commit()
      os.remove(upload.filename)
      return redirect(url_for('auth.contact', UserID=g.user[0]))

  
