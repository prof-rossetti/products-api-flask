import os
import pytest

from products_api import create_app

@pytest.fixture
def app():
    os.environ["FLASK_ENV"] = "test"
    app = create_app()
    return app

@pytest.fixture
def client(app):
    return app.test_client()
