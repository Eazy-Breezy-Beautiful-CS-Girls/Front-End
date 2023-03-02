from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:ezbreezy@database-2.cjv1pfdwijy3.us-east-2.rds.amazonaws.com:3306/database-2'
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
