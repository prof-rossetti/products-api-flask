import os
from dotenv import load_dotenv

from db import products_csv_filename, seed_products_file

if __name__ == "__main__":
    load_dotenv()
    app_env = os.environ.get("FLASK_ENV") or "development"
    csv_filename = products_csv_filename(app_env)
    print(f"SEEDING PRODUCTS FILE: {csv_filename}")
    seed_products_file(filename=csv_filename)