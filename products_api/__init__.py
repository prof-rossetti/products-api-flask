from dotenv import load_dotenv
from flask import Flask, jsonify
import os

from products_api.home_routes import home_routes
from products_api.product_routes import product_routes
from products_api.db import products_csv_filename



def create_app():
    load_dotenv()
    app_env=os.getenv("FLASK_ENV") or "development"
    csv_filename = f"products_{app_env}.csv"
    secret_key = os.getenv("SECRET_KEY") or "my super secret"
    testing = True if app_env == "test" else False

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        ENV=app_env,
        SECRET_KEY=secret_key,
        CSV_FILENAME=csv_filename,
        TESTING=testing
    )

    @app.errorhandler(400)
    def bad_request(message="Not Found"):
        response = jsonify({"status": 400, "message": message})
        response.status_code = 404
        return response

    app.register_blueprint(home_routes)
    app.register_blueprint(product_routes)

    return app







if __name__ == "__main__":
    app = create_app()
    app.run()
