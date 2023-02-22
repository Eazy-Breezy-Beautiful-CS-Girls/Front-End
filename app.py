from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY']='sh its a secret'

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/about.html', methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/causes.html', methods=['GET'])
def causes():
    return render_template('causes.html')

@app.route('/blog.html', methods=['GET','POST'])
def blog():
    return render_template('blog.html')

@app.route('/contact.html', methods=['GET'])
def contact():
    return render_template('contact.html')

@app.route('/single.html', methods=['GET'])
def single():
    return render_template('single.html')
