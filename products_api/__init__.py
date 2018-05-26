from flask import Flask

app = Flask(__name__)

from products_api import routes

app.run # app.run(debug=True)
