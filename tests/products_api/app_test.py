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
    assert "Products API (Flask)" in str(response.data)

def test_hello(client):
    response = client.get('/hello')
    assert "Hello World" in str(response.data)

def test_hello_with_params(client):
    response = client.get('/hello?name=Jordan')
    assert "Hello, Jordan" in str(response.data)

#
# PRODUCTS
#

# LIST PRODUCTS

def test_list_products(client):
    response = client.get('/products')
    response_body = json.loads(response.data)
    assert response.status_code == 200
    assert isinstance(response_body, list)
    assert len(response_body) == 20
    assert isinstance(response_body[0], dict)

# SHOW PRODUCT

def test_show_product(client):
    response = client.get('/products/1')
    response_body = json.loads(response.data) # or response.get_json()
    attributes = list(response_body.keys())
    assert response.status_code == 200
    assert isinstance(response_body, dict)
    assert attributes == ["aisle", "department", "id", "name", "price"]
    assert int(response_body["id"]) == 1

def test_show_product_failure_redirect(client):
    response = client.get('/products/100', follow_redirects=False)
    assert response.status_code == 302
    assert response.location == "http://localhost/" # redirects to this URL
    assert "You should be redirected automatically to target URL" in str(response.data)

def test_show_product_failure_flash(client):
    response = client.get('/products/100', follow_redirects=True)
    assert response.status_code == 200
    assert "Oops, couldn&#39;t find a product with an identifier of 100. Please try again." in str(response.data)
