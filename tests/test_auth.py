import pytest
import io

@pytest.mark.parametrize('data, expected_status, expected_message', [
    ({'pic': (io.BytesIO(b'my file contents'), 'valid_file.jpg')}, 302, b'Redirecting'),
    ({'pic': (io.BytesIO(b'my file contents'), 'invalid_file.txt')}, 400, b'Invalid file format'),
    ({'pic': None}, 400, b'No file selected'),
    ({'pic': (io.BytesIO(b'my file contents'), 'valid_file.jpg')}, 401, b'Unauthorized user'),
])
def test_upload_file(client, mocker, data, expected_status, expected_message):
    mocker.patch('builtins.open', mocker.mock_open(read_data=b'file_content'))
    response = client.post('/uploader', data=data)
    assert response.status_code == expected_status
    assert expected_message in response.data
