import datetime
from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for
from FrontEnd.auth import login_required

from FrontEnd.database import get_db

bp = Blueprint("fund", __name__)

@bp.route('/', methods=['GET'])
def index():
    with get_db().cursor() as cursor:
        cursor.execute('SELECT * FROM Funds')
        funds = cursor.fetchmany(3)
        return render_template('index.html', funds=funds)

@bp.route('/causes', methods=['GET'])
def causes():
    return render_template('causes.html')

@bp.route('/fundraisers/<string:fund_name>', methods=['GET','POST'])
def fundraisers(fund_name):
    if request.method == 'POST':
        title = fund_name
        amount = request.form.get('amount')
        comment = request.form.get('comment')
        get_db().cursor().execute('UPDATE Funds SET FundRaised = FundRaised+%s WHERE FundName = %s',(amount,title))
        get_db().commit()
        if g.user:
            get_db().cursor().execute('INSERT INTO Donations (FundName, UserID, DonoAmount, DonoTime, DonoComment) VALUES (%s,%s,%s,%s,%s)',(title,g.user,amount,datetime.datetime.now(),comment))
            get_db().commit()
        return redirect(url_for('index'))
    with get_db().cursor() as cursor:
        cursor.execute('SELECT * FROM Funds WHERE FundName = %s',(fund_name))
        fund = cursor.fetchone()
        return render_template('fundraisers.html', fund=fund)

@bp.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'GET':
        return render_template('form.html')
    elif request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        goal = int(request.form.get('goal'))
        user_id = g.user[0]
        end_date = request.form.get('date')
        start_date = datetime.now()
        get_db().cursor().execute('INSERT IGNORE INTO Funds (FundName, FundEndDate, FundDesc, FundGoal, FundRaised, FundStartDate) VALUES (%s, %s, %s, %s, 0, %s);\
                                  INSERT IGNORE INTO UserFundLink (UserId,FundName) VALUES (%s,%s);', (title,end_date,description,goal,start_date,user_id,title))
        get_db().commit()
        return redirect(url_for('index'))
    
@bp.route('/donation', methods=['GET', 'POST'])
def donate():
    if request.method == 'POST':
        title = request.form.get('title')
        amount = request.form.get('amount')
        comment = request.form.get('comment')
        get_db().cursor().execute('UPDATE Funds SET FundRaised = FundRaised+%s WHERE FundName = %s',(amount,title))
        get_db().commit()
        if g.user:
            get_db().cursor().execute('INSERT INTO Donations (FundName, UserID, DonoAmount, DonoTime, DonoComment) VALUES (%s,%s,%s,%s,%s)',(title,g.user,amount,datetime.datetime.now(), comment))
            get_db().commit()
        return redirect(url_for('index'))
    return render_template('donation.html')
        