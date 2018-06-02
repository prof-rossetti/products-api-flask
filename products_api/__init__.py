from dotenv import load_dotenv
from flask import Flask, jsonify
import os

from products_api.db import products_csv_filename
from products_api.error_handlers import error_handlers
from products_api.home_routes import home_routes
from products_api.product_routes import product_routes

def create_app():
    load_dotenv()

    app = Flask(__name__, instance_relative_config=True)

    app_env = os.getenv("FLASK_ENV") or "development"
    secret_key = os.getenv("SECRET_KEY") or "my super secret"
    csv_filename = products_csv_filename(app_env)
    testing = True if app_env == "test" else False
    app.config.from_mapping(ENV=app_env, SECRET_KEY=secret_key, CSV_FILENAME=csv_filename, TESTING=testing)

    app.register_blueprint(error_handlers)
    app.register_blueprint(home_routes)
    app.register_blueprint(product_routes)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run()
