# Products API (Flask)

[![Build Status](https://travis-ci.com/prof-rossetti/products-api-flask.svg?branch=master)](https://travis-ci.com/prof-rossetti/products-api-flask)

An example REST API, built in Python with the Flask framework.

## API Documentation

### Products

#### List Products

    GET /products

Example Request:

```sh
curl http://127.0.0.1:5000/products
curl https://nyu-info-2335-products-api.herokuapp.com/products
curl https://nyu-info-2335-products-api-csv.herokuapp.com/products
```

Example Response:

```json
[
  {"aisle":"cookies cakes", "department":"snacks", "id":1, "name":"Chocolate Sandwich Cookies", "price":3.5},
  {"aisle":"refrigerated", "department":"beverages", "id":2, "name":"Peach Mango Juice", "price":1.99},
  {"aisle":"juice nectars", "department":"beverages", "id":3, "name":"Pomegranate Cranberry & Aloe Vera Enrich Drink", "price":4.25}
]
```

#### Show Product

    GET /products/:id

Example Request:

```sh
curl http://127.0.0.1:5000/products/1
curl https://nyu-info-2335-products-api.herokuapp.com/products/1
curl https://nyu-info-2335-products-api-csv.herokuapp.com/products/1
```

Example Response:

```json
{
  "aisle": "cookies cakes",
  "department": "snacks",
  "id": 1,
  "name": "Chocolate Sandwich Cookies",
  "price": 3.5
}
```

#### Create Product

    POST /products

Example Request:

```sh
curl -X POST http://127.0.0.1:5000/products -d '{"aisle":"pending assignment", "department": "pending assignment", "name": "My New Product!", "price": "100.00"}'

curl -X POST https://nyu-info-2335-products-api-csv.herokuapp.com/products -d '{"aisle":"pending assignment", "department": "pending assignment", "name": "My New Product!", "price": "100.00"}'
```

Example Response Body:

```json
{
  "aisle": "pending assignment",
  "department": "pending assignment",
  "id": 4,
  "name": "My New Product!",
  "price": 100.00
}
```

























#### Update Product

    PUT /products/:id

Example Request:

```sh
curl http://127.0.0.1:5000/products/4
curl https://nyu-info-2335-products-api-csv.herokuapp.com/products/4
```

Example Response Body:

```json
{
  "aisle": "grains rice dried goods",
  "department": "dry goods pasta",
  "id": 4,
  "name": "Organic Whole Wheat Pasta",
  "price": 100.00
}
```








#### Destroy Product

    DELETE /products/:id

Example Request:

```sh
curl http://127.0.0.1:5000/products/4
curl https://nyu-info-2335-products-api-csv.herokuapp.com/products/4
```

Example Response Body:

```json
{
  "message": "Deleted Successfully"
}
```






























## [Contributing](/CONTRIBUTING.md)

## [Deploying](/DEPLOYING.md)

## [License](/LICENSE.md)
