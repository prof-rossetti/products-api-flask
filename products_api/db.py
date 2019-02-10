import csv
import os

#
# PRODUCTS DATABASE
#

def all_products():
    return read_products_from_file()

def find_product(id, all_products):
    matching_products = [product for product in all_products if int(product["id"]) == int(id)]
    try:
        matching_product = matching_products[0]
    except IndexError as e:
        matching_product = None
    return matching_product

def auto_incremented_id(products):
    if len(products) == 0:
        return 1
    else:
        product_ids = [int(p["id"]) for p in products]
        return max(product_ids) + 1 # use the next available integer

def is_valid_price(my_price):
    try:
        float(my_price)
        return True
    except Exception as e:
        return False

#
# CSV FILE DATASTORE
#

def products_csv_filename(app_env):
    return f"products_{app_env}.csv"

def read_products_from_file(filename="products_development.csv"):
    filepath = os.path.join(os.path.dirname(__file__), "db", filename)
    products = []
    with open(filepath, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        for ordered_dict in reader:
            products.append(dict(ordered_dict))
    return products

def write_products_to_file(products=[], filename="products_development.csv"):
    filepath = os.path.join(os.path.dirname(__file__), "db", filename)
    with open(filepath, "w") as csv_file:
        csv_headers = ["id", "name", "aisle", "department", "price"]
        writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
        writer.writeheader()
        for product in products:
            writer.writerow(product)
    return products

def reset_products_file(filename="products_development.csv", from_filename="products_empty.csv"):
    products = read_products_from_file(from_filename)
    new_products = write_products_to_file(products, filename)
    return new_products

def seed_products_file(filename="products_development.csv", from_filename="products_default.csv"):
    products = reset_products_file(filename=filename, from_filename=from_filename)
    return products
