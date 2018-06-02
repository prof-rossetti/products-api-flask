from flask import (
    Blueprint,
    current_app,
    flash,
    jsonify,
    render_template,
    redirect,
    request,
    url_for
)

from products_api.db import (
    all_products,
    find_product,
    is_valid_price,
    auto_incremented_id,
    write_products_to_file
)

#
# HOME
#

home_routes = Blueprint('home_routes', __name__)

@home_routes.route('/')
def index():
    current_app.logger.info("INDEX")
    return render_template('index.html')

@home_routes.route('/hello')
def hello(name=None):
    current_app.logger.info("HELLO")
    if "name" in request.args:
        name = request.args["name"]
    return render_template('hello.html', name=name)

#
# PRODUCTS
#

product_routes = Blueprint('product_routes', __name__)

# GET /products
@product_routes.route('/products')
@product_routes.route('/products.json')
def list_products():
    current_app.logger.info("LIST PRODUCTS")
    products = all_products()
    return jsonify(products)

# GET /products/:id
@product_routes.route('/products/<int:id>')
@product_routes.route('/products/<int:id>.json')
def show_product(id):
    current_app.logger.info(f"SHOW PRODUCT {id}")
    product = find_product(id)
    if product == None:
        flash( f"Oops, couldn't find a product with an identifier of {id}. Please try again.", "error")
        return redirect(url_for('home_routes.index'))
    else:
        return jsonify(product)










@product_routes.errorhandler(400)
def bad_request(message="Not Found"):
    response = jsonify({"status": 400, "message": message})
    response.status_code = 404
    return response






# POST /products
@product_routes.route('/products', methods=["POST"])
@product_routes.route('/products.json', methods=["POST"])
def create_product():
    current_app.logger.info("CREATE PRODUCT")
    new_product = request.get_json(force=True) # doesn't require request headers to specify content-type of json
    if is_valid_price(new_product["price"]) == False:
        return bad_request(message=f"OOPS. That product price ({new_product['price']}) is not valid. Expecting a price like 4.99 or 0.77. Please try again.")
    else:
        products = all_products()
        new_product["id"] = auto_incremented_id(products)
        products.append(new_product)
        write_products_to_file(products=products)
        return jsonify(new_product)
