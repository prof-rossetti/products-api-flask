import pytest

from products_api import create_app

@pytest.fixture
def app():
    app = create_app(csv_filename="products_test.csv")
    return app

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()
