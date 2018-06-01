from flask import Flask, jsonify, render_template, flash, redirect, url_for, request

from products_api import app
from products_api.db import all_products, find_product

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
    products = all_products()
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

# POST /products
#@app.route('/products', methods=["POST"])
#@app.route('/products.json', methods=["POST"])
#def create_product():
#    app.logger.info("CREATE PRODUCT")
#    products = read_products_from_file()
#
#    new_product = request.args[""]
#    if is_valid_price(new_product["price"]) == False:
#        flash( f"Oops, couldn't find a product with an identifier of {id}. Please try again.", "error")
#        return redirect(url_for('index'))
#    else:
#        products.append(new_product)
#        write_products_to_file(products)
#        return jsonify(new_product)
