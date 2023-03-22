import pymysql

conn = pymysql.connect(
        host= 'database-2.cjv1pfdwijy3.us-east-2.rds.amazonaws.com', 
        port = 3306,
        user = 'admin', 
        password = 'ezbreezy',
        db = 'mydb',
        )

# insert query
def insert_details(name,password,email):
    cur=conn.cursor()
    cur.execute("INSERT IGNORE INTO UserInfo (UserID,Password,Email) VALUES (%s,%s,%s)", (name,password,email))
    conn.commit()
#read the data
def get_details(username,password):
    cur=conn.cursor()
    cur.execute('SELECT * FROM UserInfo WHERE UserID = %s AND Password = %s', (username,password))
    details = cur.fetchall()
    return details
def add_login(id):
    cur=conn.cursor()
    cur.execute("INSERT IGNORE INTO LoggedIn (UserID) VALUES (%s)", (id))
    conn.commit()
def get_login(id):
    cur=conn.cursor()
    cur.execute('SELECT * FROM LoggedIn WHERE UserID = %s', (id))
    details = cur.fetchall()
    return details