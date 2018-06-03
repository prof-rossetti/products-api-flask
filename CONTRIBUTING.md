# Contributor's Guide

## Prerequisites

Install Python 3.6 and Pip and Pipenv.

## Installation

Download source code:

```sh
git clone git@github.com:prof-rossetti/products-api-flask.git
cd products-api-flask/
```

Install package dependencies, including Flask:

```sh
pipenv install
```

All following commands assume you are running them from within a Pipenv virtual environment:

```sh
pipenv shell
```

## Setup

Before you run this application for the first time (and anytime you want to clear all records from the database), reset the database:

```sh
FLASK_ENV=development python3 products_api/reset.py
```

Optionally populate, or "seed", the database with the default records:

```sh
FLASK_ENV=development python3 products_api/seed.py
```

## Usage

Start a local webserver:

```sh
FLASK_APP=products_api FLASK_ENV=development flask run
```

## Testing

Run tests:

```sh
pytest
```
