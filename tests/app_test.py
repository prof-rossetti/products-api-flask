import os
import pytest

from products_api import create_app

def test_app_config():
    #setup:
    app = create_app()
    assert app.testing == False
    #test:
    os.environ["FLASK_ENV"] = "test"
    csv_filename = "products_test.csv"
    app = create_app(csv_filename=csv_filename)
    assert app.config["CSV_FILENAME"] == csv_filename
    assert app.config["ENV"] == "test"
    assert app.config["TESTING"] == True
    assert app.testing == True

#def test_client(client):
#    pytest.set_trace()
