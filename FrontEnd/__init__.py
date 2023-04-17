from flask import Flask

def create_app():
    app = Flask(__name__)
    app.secret_key = 'super secret string'  # Change this!
    
    from FrontEnd import database as db
    
    db.init_app(app)
    
    from FrontEnd import auth, fund
    
    app.register_blueprint(auth.bp)
    app.register_blueprint(fund.bp)
    # import stripe
    # stripe.api_key = "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"

    app.add_url_rule("/", endpoint="index")
    
    return app