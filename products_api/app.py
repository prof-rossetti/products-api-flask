from dotenv import load_dotenv
from flask import Flask
import os

load_dotenv()

app = Flask(__name__)

app.secret_key = os.getenv("SECRET_KEY") or "my super secret"

#app.config['MY_ENV'] = os.getenv("MY_ENV") or "development"
