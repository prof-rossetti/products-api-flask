# Products API (Flask)

[![Build Status](https://travis-ci.com/prof-rossetti/products-api-flask.svg?branch=master)](https://travis-ci.com/prof-rossetti/products-api-flask)

An example REST API, built in Python with the Flask  framework.

Different branches of this repository contain different versions of this application. These different versions exist to illustrate differences in datastores.

branch | heroku app | description
--- | --- | ---
`master` | https://nyu-info-2335-products-api.herokuapp.com/ | Uses an in-memory datastore, only supports read operations (i.e. "List Products" and "Show Product").
`csv` | https://nyu-info-2335-products-api-csv.herokuapp.com/ | Uses a CSV file datastore, supports all operations.

## Usage

### Endpoints

#### List Products

Request:

    GET /products

Example Response:

```json
[
  {"aisle":"cookies cakes","department":"snacks","id":1,"name":"Chocolate Sandwich Cookies","price":3.5},
  {"aisle":"refrigerated","department":"beverages","id":11,"name":"Peach Mango Juice","price":1.99},
  {"aisle":"juice nectars","department":"beverages","id":20,"name":"Pomegranate Cranberry & Aloe Vera Enrich Drink","price":4.25}
]
```

#### Show Product

Request:

    GET /products/:id

Example Response:

```json
{
  "aisle":"refrigerated",
  "department":"beverages",
  "id":11,
  "name":"Peach Mango Juice",
  "price":1.99
}
```


#### Create Product

Request:

    POST /products

Example Response:

```json
// todo
```

#### Update Product

Request:

    PUT /products/:id

Response:

```json
// todo
```

#### Destroy Product

Request:

    DELETE /products/:id

Example Response:

```json
// todo
```


## [Contributing](/CONTRIBUTING.md)

## [Deploying](/DEPLOYING.md)

## [License](/LICENSE.md)
