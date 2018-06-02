
from products_api.db import seed_products_file

# GET /products/:id

def test_show_product(client):
    #setup:
    seed_products_file(filename="products_test.csv")
    #test:
    response = client.get('/products/1')
    response_body = response.get_json()
    attributes = list(response_body.keys())
    assert response.status_code == 200
    assert isinstance(response_body, dict)
    assert attributes == ["aisle", "department", "id", "name", "price"]
    assert int(response_body["id"]) == 1

def test_show_product_failure_redirect(client):
    #setup:
    seed_products_file(filename="products_test.csv")
    #test:
    response = client.get('/products/100', follow_redirects=False)
    assert response.status_code == 302
    assert response.location == "http://localhost/" # redirects to this URL
    assert "You should be redirected automatically to target URL" in str(response.data)

def test_show_product_failure_flash(client):
    #setup:
    seed_products_file(filename="products_test.csv")
    #test:
    response = client.get('/products/100', follow_redirects=True)
    assert response.status_code == 200
    assert "OOPS. Couldn&#39;t find a product with an identifier of 100. Please try again." in str(response.data)
