
from flask import Flask, jsonify, render_template

from products_api import app
from products_api.db import products, find_product

#
# HOME
#

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

#
# PRODUCTS
#

# GET /products
@app.route('/products')
@app.route('/products.json')
def list_products():
    return jsonify(products)

# GET /products/:id
@app.route('/products/<int:id>')
@app.route('/products/<int:id>.json')
def show_product(id):
    product = find_product(id)
    return jsonify(product)
