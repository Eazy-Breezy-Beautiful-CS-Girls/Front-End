from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for
import functools
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
    return redirect(url_for('index'))

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if not get_db().cursor().execute("SELECT * FROM UserInfo WHERE UserID = %s AND Password = %s",(username, password)) == 0:
            get_db().cursor().execute("INSERT IGNORE INTO LoggedIn (UserID) VALUES (%s)",(username))
            get_db().commit()
            flash('Logged in successfully.')
            session.clear()
            session['user_id'] = username
            return redirect(url_for('index'))
        flash('Login failed')
        return render_template('login.html')
    
@bp.route('/Sign-up', methods=['GET','POST'])
def Signup():
    if request.method == 'GET':
        return render_template('Sign-up.html')
    elif request.method == 'POST':
        UserID = request.form.get('username'),
        Password = request.form.get('password'),
        Email = request.form.get('email')
        get_db().cursor().execute("INSERT IGNORE INTO UserInfo (UserID,Password,Email) VALUES (%s,%s,%s)", (UserID,Password,Email))
        get_db().commit()
        return login()
