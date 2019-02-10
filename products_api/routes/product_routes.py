from flask import Blueprint, current_app, flash, jsonify, redirect, request, url_for

from products_api.db import read_products_from_file, find_product, write_products_to_file, is_valid_price, auto_incremented_id
from products_api.error_handlers import not_found, bad_request

product_routes = Blueprint("product_routes", __name__)

# GET /products
@product_routes.route('/products')
@product_routes.route('/products.json')
def list_products():
    current_app.logger.info("LISTING PRODUCTS")

    products = read_products_from_file(current_app.config["CSV_FILENAME"])
    return jsonify(products)

# GET /products/:id
@product_routes.route('/products/<int:id>')
@product_routes.route('/products/<int:id>.json')
def show_product(id):
    current_app.logger.info(f"SHOWING PRODUCT {id}")

    products = read_products_from_file(current_app.config["CSV_FILENAME"])
    product = find_product(id, products)
    if product == None:
        flash( f"OOPS. Couldn't find a product with an identifier of {id}. Please try again.", "error")
        return redirect(url_for('home_routes.index'))

    return jsonify(product)

# POST /products
@product_routes.route('/products', methods=["POST"])
@product_routes.route('/products.json', methods=["POST"])
def create_product():
    current_app.logger.info("CREATING PRODUCT")

    new_product = request.get_json(force=True) # doesn't require request headers to specify content-type of json
    if is_valid_price(new_product["price"]) == False:
        return bad_request(message=f"OOPS. That product price is not valid ({new_product['price']}). Expecting a price like 4.99 or 0.77. Please try again.")

    products = read_products_from_file(current_app.config["CSV_FILENAME"])
    new_product["id"] = auto_incremented_id(products)
    products.append(new_product)
    write_products_to_file(products=products, filename=current_app.config["CSV_FILENAME"])
    return jsonify(new_product)

# PUT/POST /products/:id
@product_routes.route('/products/<int:id>', methods=["PUT", "POST"])
@product_routes.route('/products/<int:id>.json', methods=["PUT", "POST"])
def update_product(id):
    current_app.logger.info(f"UPDATING PRODUCT {id}")

    products = read_products_from_file(current_app.config["CSV_FILENAME"])
    product = find_product(id, products)
    if product == None:
        return not_found(message="OOPS. Couldn't find a product with that identifier ({id}). Please try again.")

    edited_product = request.get_json(force=True) # doesn't require request headers to specify content-type of json
    current_app.logger.info(edited_product)
    edited_product["id"] = id # don't allow client to overwrite id :-)
    if is_valid_price(edited_product["price"]) == False:
        return bad_request(message=f"OOPS. That product price is not valid ({edited_product['price']}). Expecting a price like 4.99 or 0.77. Please try again.")

    products[products.index(product)] = edited_product
    write_products_to_file(products=products, filename=current_app.config["CSV_FILENAME"])
    return jsonify(edited_product)

# DELETE /products/:id
@product_routes.route('/products/<int:id>', methods=["DELETE"])
@product_routes.route('/products/<int:id>.json', methods=["DELETE"])
def destroy_product(id):
    current_app.logger.info(f"DESTROYING PRODUCT {id}")

    products = read_products_from_file(current_app.config["CSV_FILENAME"])
    product = find_product(id, products)
    if product == None:
        return not_found(message="OOPS. Couldn't find a product with that identifier ({id}). Please try again.")

    del products[products.index(product)]
    write_products_to_file(products=products, filename=current_app.config["CSV_FILENAME"])
    return jsonify({"message": "Product Deleted Successfully"})
