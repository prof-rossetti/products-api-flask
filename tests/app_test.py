import os
import pytest

from products_api import create_app

def test_app_default_config():
    app = create_app()
    assert app.config["ENV"] == "development"
    assert app.config["CSV_FILENAME"] == "products_development.csv"
    assert app.config["TESTING"] == False
    assert app.testing == False

def test_app_config():
    os.environ["FLASK_ENV"] = "test"
    app = create_app()
    assert app.config["CSV_FILENAME"] == "products_test.csv"
    assert app.config["ENV"] == "test"
    assert app.config["TESTING"] == True
    assert app.testing == True
