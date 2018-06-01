
from products_api.db import (
    read_products_from_file,
    write_products_to_file,
    reset_products_file
)

def test_read_products_from_file():
    products = read_products_from_file(filename="products_default.csv")
    assert len(products) == 20

def test_write_products_to_file():
    # setup:
    products = reset_products_file(filename="products_test.csv", from_filename="products_default.csv")
    assert len(products) == 20
    # test:
    products = write_products_to_file(products=[], filename="products_test.csv")
    assert len(products) == 0

def test_reset_products_file():
    # setup:
    products = reset_products_file(filename="products_test.csv", from_filename="products_empty.csv")
    assert len(products) == 0
    # test:
    products = reset_products_file(filename="products_test.csv", from_filename="products_default.csv")
    assert len(products) == 20
