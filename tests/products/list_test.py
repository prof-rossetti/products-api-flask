from products_api.db import reset_products_file

# GET /products

def test_list_products(client):
    #setup:
    products = reset_products_file(filename="products_test.csv", from_filename="products_default.csv")
    assert len(products) == 20
    #test:
    response = client.get('/products')
    response_body = response.get_json()
    assert response.status_code == 200
    assert isinstance(response_body, list)
    assert len(response_body) == 20
    assert isinstance(response_body[0], dict)
