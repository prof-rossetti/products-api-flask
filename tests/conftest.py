import pytest # use pytest.set_trace() to drop an interactive breakpoint

#from products_api import create_app

#@pytest.fixture
#def app():
#    app = create_app(app_env="test", csv_filepath="products_test.csv")
#    return app
#
## adapted from https://serge-m.github.io/testing-json-responses-in-Flask-REST-apps-with-pytest.html
#@pytest.fixture
#def client(request):
#    test_client = app.test_client()
#    def teardown():
#        pass # databases and resourses have to be freed at the end. But so far we don't have anything
#    request.addfinalizer(teardown)
#    return test_client
