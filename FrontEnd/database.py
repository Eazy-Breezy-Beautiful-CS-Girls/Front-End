import pymysql
from flask import g


def get_db():
    if "db" not in g:
        conn = pymysql.connect(
        host= 'database-2.cjv1pfdwijy3.us-east-2.rds.amazonaws.com', 
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

# # insert query
# def insert_details(name,password,email):
#     cur=conn.cursor()
#     cur.execute("INSERT IGNORE INTO UserInfo (UserID,Password,Email) VALUES (%s,%s,%s)", (name,password,email))
#     conn.commit()
# #read the data
# def get_details(username,password):
#     cur=conn.cursor()
#     cur.execute('SELECT * FROM UserInfo WHERE UserID = %s AND Password = %s', (username,password))
#     details = cur.fetchall()
#     return details
# def add_login(id):
#     cur=conn.cursor()
#     cur.execute("INSERT IGNORE INTO LoggedIn (UserID) VALUES (%s)", (id))
#     conn.commit()
# def get_login(id):
#     cur=conn.cursor()
#     cur.execute('SELECT * FROM LoggedIn WHERE UserID = %s', (id,))
#     details = cur.fetchone()
#     return details
    