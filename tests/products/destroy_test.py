from products_api.db import seed_products_file

# DELETE /products/:id

def test_delete_product(client):
    #setup:
    seed_products_file(filename="products_test.csv")
    #test:
    response = client.delete('/products/4')
    response_body = response.get_json()
    assert response.status_code == 200
    assert isinstance(response_body, dict)
    assert "Deleted Successfully" in response_body["message"]

def test_delete_product_not_found(client):
    #setup:
    seed_products_file(filename="products_test.csv")
    #test:
    response = client.delete('/products/99')
    assert response.status_code == 404
    response_body = response.get_json()
    assert isinstance(response_body, dict)
    assert "OOPS. Couldn't find a product with that identifier" in response_body["message"]
