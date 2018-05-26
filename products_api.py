from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'Products API (Flask)'

#
# PRODUCTS
#

@app.route('/products/<int:id>') # @app.route('/products/<int:id>', methods=['GET'])
def show_product(id):
    return jsonify({"id": id, "name": "Cookies", "description": "A bag of cookies."})
