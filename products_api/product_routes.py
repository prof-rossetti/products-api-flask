from flask import Blueprint, current_app, flash, jsonify, redirect, request, url_for

from products_api.db import read_products_from_file, find_product, write_products_to_file, is_valid_price, auto_incremented_id

product_routes = Blueprint('product_routes', __name__)

# GET /products
@product_routes.route('/products')
@product_routes.route('/products.json')
def list_products():
    current_app.logger.info("LIST PRODUCTS")
    products = read_products_from_file(current_app.config["CSV_FILENAME"])
    return jsonify(products)

# GET /products/:id
@product_routes.route('/products/<int:id>')
@product_routes.route('/products/<int:id>.json')
def show_product(id):
    current_app.logger.info(f"SHOW PRODUCT {id}")
    products = read_products_from_file(current_app.config["CSV_FILENAME"])
    product = find_product(id, products)
    if product == None:
        flash( f"Oops, couldn't find a product with an identifier of {id}. Please try again.", "error")
        return redirect(url_for('home_routes.index'))
    else:
        return jsonify(product)

# POST /products
@product_routes.route('/products', methods=["POST"])
@product_routes.route('/products.json', methods=["POST"])
def create_product():
    current_app.logger.info("CREATE PRODUCT")
    new_product = request.get_json(force=True) # doesn't require request headers to specify content-type of json
    if is_valid_price(new_product["price"]) == False:
        return bad_request(message=f"OOPS. That product price ({new_product['price']}) is not valid. Expecting a price like 4.99 or 0.77. Please try again.")
    else:
        products = read_products_from_file(current_app.config["CSV_FILENAME"])
        new_product["id"] = auto_incremented_id(products)
        products.append(new_product)
        write_products_to_file(products=products, filename=current_app.config["CSV_FILENAME"])
        return jsonify(new_product)
