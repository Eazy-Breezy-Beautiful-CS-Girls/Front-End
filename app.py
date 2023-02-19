from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY']='sh its a secret'

@app.route('/')
def index():
    return render_template('index.html')
