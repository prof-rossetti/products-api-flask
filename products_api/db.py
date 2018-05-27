import csv
import os

#
# PRODUCTS DATABASE
#

def all_products():
    products = []
    filepath = os.path.join(os.path.dirname(__file__), "db/products.csv")
    with open(filepath, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        for ordered_dict in reader:
            products.append(dict(ordered_dict))
    return products

def find_product(id):
    products = all_products()
    matching_products = [product for product in products if int(product["id"]) == int(id)]
    try:
        matching_product = matching_products[0]
    except IndexError as e:
        matching_product = None
    return matching_product
