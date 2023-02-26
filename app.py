from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://admin:ezbreezy@{endpoint}/{db instance name}'

db = SQLAlchemy(app)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/about.html', methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/causes.html', methods=['GET'])
def causes():
    return render_template('causes.html')

@app.route('/login.html', methods=['GET','POST'])
def login():
    return render_template('login.html')

@app.route('/contact.html', methods=['GET'])
def contact():
    return render_template('contact.html')

@app.route('/single.html', methods=['GET'])
def single():
    return render_template('single.html')
