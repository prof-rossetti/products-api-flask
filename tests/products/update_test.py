
from products_api.db import seed_products_file

# PUT/POST /products

def test_update_product(client):
    #setup:
    seed_products_file(filename="products_test.csv", from_filename="products_example.csv")
    #test:
    id = 5
    edited_product = {
        "id":"50",
        "aisle":"updated aisle",
        "department": "updated dept.",
        "name": "Updated Product!",
        "price": "123.45"
    }
    response = client.put(f"/products/{id}.json", json=edited_product)
    assert response.status_code == 200
    response_body = response.get_json()
    assert isinstance(response_body, dict)
    assert response_body["id"] == id
    assert response_body["name"] == "Updated Product!"

def test_update_product_not_found(client):
    #setup:
    seed_products_file(filename="products_test.csv", from_filename="products_example.csv")
    #test:
    id = 999
    edited_product = {
        "id":"50",
        "aisle":"updated aisle",
        "department": "updated dept.",
        "name": "Updated Product!",
        "price": "123.45"
    }
    response = client.put(f"/products/{id}.json", json=edited_product)
    assert response.status_code == 404
    response_body = response.get_json()
    assert isinstance(response_body, dict)
    assert "OOPS. Couldn't find a product with that identifier" in response_body["message"]

def test_update_product_invalid_price(client):
    #setup:
    seed_products_file(filename="products_test.csv", from_filename="products_example.csv")
    #test:
    id = 5
    edited_product = {
        "id":"50",
        "aisle":"updated aisle",
        "department": "updated dept.",
        "name": "Updated Product!",
        "price": "$123.45"
    }
    response = client.put(f"/products/{id}.json", json=edited_product)
    assert response.status_code == 400
    response_body = response.get_json()
    assert isinstance(response_body, dict)
    assert "OOPS. That product price is not valid" in response_body["message"]
