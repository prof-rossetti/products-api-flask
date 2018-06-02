
# POST /products

def test_create_product(client):
    new_product = {
        "aisle":"pending assignment",
        "department": "pending assignment",
        "name": "My New Product!",
        "price": "100.00"
    }
    response = client.post('/products.json', json=new_product)
    response_body = response.get_json()
    assert response.status_code == 200
    assert isinstance(response_body, dict)

def test_create_product_invalid_price(client):
    new_product = {
        "aisle":"pending assignment",
        "department": "pending assignment",
        "name": "My New Product!",
        "price": "$123"
    }
    response = client.post('/products.json', json=new_product)
    response_body = response.get_json()
    assert response.status_code == 400
    assert isinstance(response_body, dict)
    assert "OOPS. That product price is not valid" in response_body["message"]
