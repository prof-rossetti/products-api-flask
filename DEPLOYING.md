# Deployer's Guide

## Prerequisites

Install the heroku command-line utility (perhaps via `brew install heroku`), then login to your heroku account with `heroku login`.

### Creating a new Server

Then create a new app server:

```sh
heroku create
```

### Configuring the Server

Generate a secret string:

```sh
python -c 'import secrets; print(secrets.token_hex(16))'
```

Then store the value (e.g. "abc123") in an environment variable:

```sh
heroku config:set SECRET_KEY="abc123"
heroku config:set FLASK_ENV=production
```

## Deploying

Deploy the source code:

```sh
git push my_remote my_branch:master
```

## Deployment Environments

### Production

Uses an in-memory datastore, only supports read operations (i.e. "List Products" and "Show Product").

To deploy:

```sh
git push heroku master
```

&nbsp; | &nbsp;
--- | ---
heroku app name: | `nyu-info-2335-products-api`
url: | https://nyu-info-2335-products-api.herokuapp.com/
git remote name: | `heroku`
git branch name: | `master`

### Production (CSV)

Uses a CSV file datastore, supports all operations.

To deploy:

```sh
git push heroku-csv csv:master
```

Migrate/seed/reset the database as necessary:

```sh
heroku run "python products_api/seed.py"
```

&nbsp; | &nbsp;
--- | ---
heroku app name: | `nyu-info-2335-products-api-csv`
url: | https://nyu-info-2335-products-api-csv.herokuapp.com/
git remote name: | `heroku-csv`
git branch name: | `csv`
