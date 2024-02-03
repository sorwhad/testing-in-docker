import requests


def test_remote_address():
    response = requests.get('http://remote_app:8890')
    assert 200 == response.status_code
