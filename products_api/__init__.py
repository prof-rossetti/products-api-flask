from dotenv import load_dotenv
import os

from products_api.app import app
import products_api.routes

load_dotenv()

app.secret_key = os.getenv("SECRET_KEY") or "my super secret"

app.run
