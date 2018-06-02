
from products_api import create_app

def test_app():
    app = create_app()
    assert app.testing == False

    app_env = "test"
    csv_filepath = "products_test.csv"
    app = create_app(app_env="test", csv_filepath=csv_filepath)
    assert app.config["CSV_FILEPATH"] == csv_filepath
    assert app.config["ENV"] == app_env
    assert app.config["TESTING"] == True
    assert app.testing == True
