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