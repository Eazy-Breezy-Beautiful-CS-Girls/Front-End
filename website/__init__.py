
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY']='sh its a secret'
    
    from .views import views
    
    app.register_blueprint(views, url_prfix='/')
    
    return app