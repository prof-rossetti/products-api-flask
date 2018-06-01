from db import reset_products_file

if __name__ == "__main__":
    print("RESETTING PRODUCTS FILE")
    reset_products_file(filename="products.csv")
    reset_products_file(filename="products_development.csv")
    reset_products_file(filename="products_test.csv")
