import pytest

def test_index(client, auth):
    response = client.get('/')
    assert b"Login" in response.data
    assert b"Sign-up" in response.data
    
    auth.login()
    response = client.get('/')
    assert b'logout' in response.data
    assert b'Profile' in response.data
    
def test_fund_page(client):
    assert client.get('/fundraisers/money').status_code == 200
    
def test_create(client, auth, app):
    auth.login()
    assert client.get('/form').status_code == 200
    client.post("/form", data={'title': 'testing', 'description': 'testing', 'goal': '300', })
    