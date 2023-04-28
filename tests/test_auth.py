from flask import g, session
import pytest
import io

from FrontEnd.database import get_db

# @pytest.mark.parametrize('pic, expected_status, expected_message', [
#     (b'valid_file.jpg', 302, b'Redirecting'),
#     ({'pic': (io.BytesIO(b'my file contents'), 'invalid_file.txt')}, 400, b'Invalid file format'),
#     ({'pic': None}, 400, b'No file selected'),
#     ({'pic': (io.BytesIO(b'my file contents'), 'valid_file.jpg')}, 401, b'Unauthorized user'),
# ])
# def test_upload_file(client, pic, expected_status, expected_message):
#     response = client.post('/uploader', data=pic)
#     assert response.status_code == expected_status
#     assert expected_message in response.data\
    

def test_signup(client,auth,app):
    assert client.get('/auth/Sign-up').status_code == 200
    response = client.post('/auth/Sign-up',
                           data={
                               'fname':'test', 
                               'lname':'testing', 
                               'username':'testing',
                               'email':'testing@realmail.com',
                               'password':'testing',
                               'auth_password':'testing'})
        
    with client:
        client.get('/')
        assert session['user_id'] == 'testing'
        assert g.user[0] == 'testing'
        auth.logout()

    with app.app_context():
        with get_db().cursor() as cursor:
            user = cursor.execute("SELECT * FROM UserInfo WHERE UserID = %s AND Password = %s",('testing', 'testing'))
            assert user != 0
        get_db().cursor().execute("DELETE FROM UserInfo WHERE UserID = 'testing'")
        get_db().commit()
    
@pytest.mark.parametrize(
    ("fname","lname","username","email","password","auth_password","message"),
    (("", "","testing","testing@realmail.com","testing","testing",b"Name Required"),
     ("test", "testing","","testing@realmail.com","testing","testing",b"User ID Required"),
     ("test", "testing","tester","","testing","testing",b"Email Required"),
     ("test", "testing","tester","testing@realmail.com","","testing",b"Password Required"),
     ("test", "testing","tester","testing@realmail.com","testing","",b"Passwords must match"))
)
def test_signup_fails(client, fname, lname, username, email, password, auth_password, message):
    response = client.post('/auth/Sign-up',
                           data={
                               'fname':fname, 
                               'lname':lname, 
                               'username':username,
                               'email':email,
                               'password':password,
                               'auth_password':auth_password})
    assert message in response.data

def test_login(client, auth):
    assert client.get('/auth/login').status_code == 200
    
    response = auth.login()
    assert response.headers['Location'] == "/"
    
    with client:
        client.get('/')
        assert session['user_id'] == 'test'
        assert g.user[0] == 'test'
        
@pytest.mark.parametrize(
    ("username", "password", "message"),
    (("a", "test", b"Login Failed"), ("test", "a", b"Login Failed"))
)
def test_login_validate_input(auth, username, password, message):
    response = auth.login(username, password)
    assert message in response.data
        
def test_logout(client, auth):
    auth.login()

    with client:
        auth.logout()
        assert "user_id" not in session
        
def test_contact(client, auth):
    response = client.get("/auth/contact/test")
    assert response.headers["Location"] == "/auth/login"
    
    auth.login()
    response = client.get("/auth/contact/test")
    
    assert b"test" in response.data
    
def test_contact_change(client, auth):
    auth.login()
    client.post('/auth/contact/test', data={'fname':'tester','lname':'testerson','email':'tester@realmail.com','bio':'this guy tests a lot'})
    
    with client:
        auth.logout()
        with get_db().cursor() as cursor:
            cursor.execute('SELECT FirstName, LastName, Email, Bio FROM UserInfo WHERE UserID = %s',('test'))
            user = cursor.fetchone()
            assert user[0] == 'tester'
            assert user[1] == 'testerson'
            assert user[2] == 'tester@realmail.com'
            assert user[3] == 'this guy tests a lot'
    
    auth.login()
    client.post('/auth/contact/test', data={'fname':'test','lname':'test','email':'test@realmail.com','bio':''})
    
    with client:
        auth.logout()
("test", "tester","tester", "")
@pytest.mark.parametrize(
    ("current_pass", "new_pass", "auth_pass","message"),
    (("a", "aoeu", "aoeu", b"Incorrect Password"),
     ("test", "tester", "testing", b"Passwords do not match"))
)
def test_contact_password_change_fails(client, auth, current_pass, new_pass, auth_pass,message):
    auth.login()
    response = client.post("/auth/contact/test", data={'c_pass':current_pass,"n_pass":new_pass,"a_pass":auth_pass})
    assert message in response.data

@pytest.mark.parametrize(
    ("current_pass", "new_pass", "auth_pass"),
    (("test", "tester", "tester"),
     ("tester", "test", "test"))
)
def test_contact_password_change(client, app, auth, current_pass, new_pass, auth_pass):
    auth.login(username='test',password=current_pass)
    client.post("/auth/contact/test", data={'c_pass':current_pass,"n_pass":new_pass,"a_pass":auth_pass})
    with client:
        auth.logout()
    with app.app_context():
        with get_db().cursor() as cursor:
            cursor.execute("SELECT Password From UserInfo WHERE UserID='test'")
            password = cursor.fetchone()
            assert password[0].encode('utf-8') == new_pass.encode('utf-8')