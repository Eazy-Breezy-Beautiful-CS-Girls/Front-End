from flask import Flask
import os

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.secret_key = 'super secret string'  # Change this!
    
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.update(test_config)
    
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    @app.route("/hello")
    def hello():
        return "Hello, World!"
    
    # register the database commands
    from FrontEnd import database as db
    
    db.init_app(app)
    
    # apply the blueprints to the app
    from FrontEnd import auth, fund
    
    app.register_blueprint(auth.bp)
    app.register_blueprint(fund.bp)

    app.add_url_rule("/", endpoint="index")
    
    return app