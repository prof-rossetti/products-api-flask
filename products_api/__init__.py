from dotenv import load_dotenv
from flask import Flask, jsonify
import os

from products_api.home_routes import home_routes
from products_api.product_routes import product_routes

load_dotenv()

def create_app(csv_filename="products_special.csv"):
    app_env= os.getenv("FLASK_ENV") or "special"
    #csv_filepath = os.path.join(os.path.dirname(__file__), "db", csv_filename)
    secret_key = os.getenv("SECRET_KEY") or "my super special secret"
    testing = True if app_env == "test" else False

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        ENV=app_env,
        SECRET_KEY=secret_key,
        CSV_FILENAME=csv_filename,
        #CSV_FILEPATH=csv_filepath,
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
