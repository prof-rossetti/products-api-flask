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

## Setup

Before you run this application for the first time (or anytime you want to reset the database), reset the database by populating it with the default products:

```sh
python3 products_api/reset.py
```

## Usage

All following commands assume you are running them from within a Pipenv virtual environment:

```sh
pipenv shell
```

Start a local webserver:

```sh
FLASK_APP=products_api FLASK_ENV=development flask run
```

## Testing

All following commands assume you are running them from within a Pipenv virtual environment:

```sh
pipenv shell
```

Run tests:

```sh
pytest
```
