import pytest
import io

@pytest.mark.parametrize('pic, expected_status, expected_message', [
    (b'valid_file.jpg', 302, b'Redirecting'),
    ({'pic': (io.BytesIO(b'my file contents'), 'invalid_file.txt')}, 400, b'Invalid file format'),
    ({'pic': None}, 400, b'No file selected'),
    ({'pic': (io.BytesIO(b'my file contents'), 'valid_file.jpg')}, 401, b'Unauthorized user'),
])
def test_upload_file(client, pic, expected_status, expected_message):
    response = client.post('/uploader', data=pic)
    assert response.status_code == expected_status
    assert expected_message in response.data

def test_signup(client, app):
    assert client.get('/auth/Sign-Up').status_code == 200
    response = client.post('/Sign-Up', )