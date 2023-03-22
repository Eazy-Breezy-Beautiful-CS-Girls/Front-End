from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for
import datetime
from FrontEnd.auth import login_required

from FrontEnd.database import get_db

bp = Blueprint("fund", __name__)

@bp.route('/', methods=['GET'])
def index():
    with get_db().cursor() as cursor:
        cursor.execute('SELECT * FROM Funds')
        funds = cursor.fetchmany(3)
        return render_template('index.html', funds=funds)

@bp.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

@bp.route('/causes', methods=['GET'])
def causes():
    return render_template('causes.html')

@bp.route('/fundraisers/<string:fund_name>', methods=['GET'])
def fundraisers(fund_name):
    with get_db().cursor() as cursor:
        cursor.execute('SELECT * FROM Funds WHERE FundName = %s',(fund_name))
        fund = cursor.fetchone()
        return render_template('fundraisers.html', fund=fund)

@bp.route('/contact/<string:UserID>', methods=['GET','POST'])
@login_required
def contact(UserID):
    if request.method == 'GET':
        with get_db().cursor() as cursor:
            cursor.execute('SELECT * FROM UserInfo WHERE UserID = %s',(UserID))
            user = cursor.fetchone()
        return render_template('contact.html', user=user)
    fname = request.form.get('fname')
    lname = request.form.get('lname')
    email = request.form.get('email')
    bio = request.form.get('bio')
    get_db().cursor().execute('UPDATE UserInfo SET FirstName = %s, LastName = %s, Email = %s, Bio = %s WHERE UserID = %s',(fname, lname, email, bio, UserID))
    get_db().commit()
    return redirect(url_for('fund.contact', UserID=UserID))

@bp.route('/single', methods=['GET'])
def single():
    return render_template('single.html')

@bp.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'GET':
        return render_template('form.html')
    elif request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        goal = int(request.form.get('goal'))
        user_id = g.user_id[0]
        get_db().cursor().execute('INSERT IGNORE INTO Funds (FundName, FundType, FundGoal, FundRaised) VALUES (%s, %s, %s, 0);\
                                  INSERT IGNORE INTO UserFundLink (%s,%s);', (title,description,goal,user_id,title))
        get_db().commit()
        return redirect(url_for('index'))

@bp.route('/donation/<string:title>', methods=['GET', 'POST'])
def donation(title=None):
    if request.method == 'POST':
        title = request.form.get('title')
        amount = request.form.get('amount')
        get_db().cursor().execute('UPDATE Funds SET FundRaised = FundRaised+%s WHERE FundName = %s',(amount,title))
        get_db().commit()
        if g.user:
            get_db().cursor().execute('INSERT IGNORE INTO Donations (FundName, UserID, DonoAmount, DonoTime) VALUES (%s,%s,%s,%s)',(title,g.user,amount,datetime.datetime.now()))
            get_db().commit()
        return redirect(url_for('index'))
    print(title)
    return render_template('donation.html', title=title)
        