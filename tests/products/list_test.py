
# GET /products

def test_list_products(client):
    response = client.get('/products')
    response_body = response.get_json()
    assert response.status_code == 200
    assert isinstance(response_body, list)
    assert len(response_body) == 20
    assert isinstance(response_body[0], dict)
