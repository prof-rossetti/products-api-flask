import json
import pytest

from products_api.app import app

# adapted from https://serge-m.github.io/testing-json-responses-in-Flask-REST-apps-with-pytest.html
@pytest.fixture
def client(request):
    test_client = app.test_client()
    def teardown():
        pass # databases and resourses have to be freed at the end. But so far we don't have anything
    request.addfinalizer(teardown)
    return test_client

#
# HOME
#

def test_index(client):
    response = client.get('/')
    assert b'Products API (Flask)' in response.data

def test_hello(client):
    response = client.get('/hello')
    assert b'Hello World' in response.data

def test_hello_with_params(client):
    response = client.get('/hello/Jordan')
    assert b'Hello, Jordan' in response.data
