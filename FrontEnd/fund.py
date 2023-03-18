from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for

from FrontEnd.database import get_db

bp = Blueprint("fund", __name__)

@bp.route('/', methods=['GET'])
def index():
    return render_template('index.html')

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

@bp.route('/Fundraiser-2', methods=['GET'])
def Fundraiser2():
    return render_template('Fundrasier-2.html')

@bp.route('/Fundraiser-3', methods=['GET'])
def Fundraiser3():
    return render_template('Fundrasier-3.html')

@bp.route('/contact', methods=['GET'])
def contact():
    return render_template('contact.html')

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
        get_db().cursor().execute('INSERT IGNORE INTO Funds (FundName, FundType, FundGoal, FundRaised) VALUES (%s, %s, %s, 0)', (title,description,goal))
        get_db().commit()
        return redirect(url_for('index'))
    