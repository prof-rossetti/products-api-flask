import csv
import os

#
# PRODUCTS DATABASE
#

def all_products():
    return read_products_from_file()

def find_product(id):
    products = all_products()
    matching_products = [product for product in products if int(product["id"]) == int(id)]
    try:
        matching_product = matching_products[0]
    except IndexError as e:
        matching_product = None
    return matching_product

#
# CSV FILE DATASTORE
#

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

def reset_products_file(from_filename="products_default.csv", filename="products_development.csv"):
    products = read_products_from_file(from_filename)
    new_products = write_products_to_file(products, filename)
    return new_products
