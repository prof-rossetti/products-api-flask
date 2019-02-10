# Contributor's Guide

## Prerequisites

  + Python 3.6 or 3.7
  + Pip
  + Anaconda 3.7 (recommended)

## Installation

Download or clone the source code:

```sh
git clone git@github.com:prof-rossetti/products-api-flask.git
```

Navigate into the repository from the command-line:

```sh
cd products-api-flask/
```

Create and activate a new virtual environment called something like "products-api-env", as necessary:

```sh
conda create -n products-api-env
conda activate products-api-env
```

Inside the virtual environment, install package dependencies, including Flask:

```sh
pip install flask gunicorn python-dotenv
```

## Setup (CSV Version Only)

Before you run this application for the first time (and anytime you want to clear all records from the CSV file), reset the it:

```sh
FLASK_ENV=development python products_api/reset.py
```

Optionally populate, or "seed", the file with the default records:

```sh
FLASK_ENV=development python products_api/seed.py
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
