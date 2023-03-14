from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for

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

@bp.route('/form', methods=['GET'])
def form():
    return render_template('form.html')