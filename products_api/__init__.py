from dotenv import load_dotenv
from flask import Flask
import os

load_dotenv()

def create_app(app_env="special", csv_filepath="products_special.csv"):

    app = Flask(__name__, instance_relative_config=True)

    print("APP INSTANCE PATH", app.instance_path)
    app.logger.info(app.instance_path)

    #app.secret_key = os.getenv("SECRET_KEY") or "my super secret"
    #app.env = os.getenv("FLASK_ENV") or "special"

    if app_env == "test": testing = True
    else: testing = False

    app.config.from_mapping(
        ENV=app_env,
        SECRET_KEY="my special secret",
        CSV_FILEPATH=csv_filepath,
        TESTING=testing
        #DATABASE= os.path.join(app.instance_path, 'products_special.csv'),
    )

    import products_api.routes

    return app
