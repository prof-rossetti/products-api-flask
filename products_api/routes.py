from flask import Flask, jsonify, render_template, flash, redirect, url_for, request

from products_api import app
from products_api.db import products, find_product

#
# HOME
#

@app.route('/')
def index():
    app.logger.info("INDEX")
    return render_template('index.html')

@app.route('/hello')
def hello(name=None):
    app.logger.info("HELLO")
    if "name" in request.args:
        name = request.args["name"]
    return render_template('hello.html', name=name)

#
# PRODUCTS
#

# GET /products
@app.route('/products')
@app.route('/products.json')
def list_products():
    app.logger.info("LIST PRODUCTS")
    return jsonify(products)

# GET /products/:id
@app.route('/products/<int:id>')
@app.route('/products/<int:id>.json')
def show_product(id):
    app.logger.info(f"SHOW PRODUCT {id}")
    product = find_product(id)
    if product == None:
        flash( f"Oops, couldn't find a product with an identifier of {id}. Please try again.", "error")
        return redirect(url_for('index'))
    else:
        return jsonify(product)
