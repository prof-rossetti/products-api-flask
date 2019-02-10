# GET /

def test_index(client):
    response = client.get('/')
    assert "Products API (Flask)" in str(response.data)

# GET /hello

def test_hello(client):
    response = client.get('/hello')
    assert "Hello World" in str(response.data)

def test_hello_with_params(client):
    response = client.get('/hello?name=Jordan')
    assert "Hello, Jordan" in str(response.data)
