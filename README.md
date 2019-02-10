# Products API (Flask)

[![Build Status](https://travis-ci.com/prof-rossetti/products-api-flask.svg?branch=master)](https://travis-ci.com/prof-rossetti/products-api-flask)

An example REST API, built in Python with the Flask framework, and deployed to a Heroku server.

Different branches of this repository contain different versions of this application, and exist to illustrate differences in datastores.

branch | heroku app | description
--- | --- | ---
[`master`](https://github.com/prof-rossetti/products-api-flask) | https://groceries-api-limited.herokuapp.com/ | A read-only version, using an in-memory datastore. Only supports the "List" and "Show" operations.
[`csv`](https://github.com/prof-rossetti/products-api-flask/tree/csv) | https://groceries-api-csv.herokuapp.com/ | A fully-functional version, using a CSV file datastore. Supports all operations.

## [API Documentation](/DOCS.md)

## [Contributing](/CONTRIBUTING.md)

## [Deploying](/DEPLOYING.md)

## [License](/LICENSE.md)
