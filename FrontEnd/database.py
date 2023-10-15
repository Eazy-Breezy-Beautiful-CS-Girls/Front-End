import pymysql
from flask import g


def get_db():
    if "db" not in g:
        conn = pymysql.connect(
        host= 'database-1.ctvfyumkix2j.us-east-2.rds.amazonaws.com', 
        port = 3306,
        user = 'admin', 
        password = 'ezbreezy',
        db = 'mydb',
        )
        g.db=conn
    return g.db

def close_db(e=None):
    """If this request connected to the database, close the
    connection.
    """
    db = g.pop("db", None)

    if db is not None:
        db.close()

def init_app(app):
    """Register database functions with the Flask app. This is called by
    the application factory.
    """
    app.teardown_appcontext(close_db)

    