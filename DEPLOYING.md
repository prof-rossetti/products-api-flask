# Deployer's Guide

## Prerequisites

Install the heroku command-line utility (perhaps via `brew install heroku`), then login to your heroku account with `heroku login`.

### Creating a new Server

Then create a new app server for each environment:

```sh
heroku create
# ... or optionally specify unique app name(s) of your own:
# heroku create -n groceries-api-limited
# heroku create -n groceries-api-csv
```

### Configuring the Server

Generate a secret string:

```sh
python -c 'import secrets; print(secrets.token_hex(16))'
```

Then store the value (e.g. "abc123") in an environment variable, and configure environment variables on each server:

```sh
heroku config:set SECRET_KEY="abc123" -a groceries-api-limited
heroku config:set FLASK_ENV="production" -a groceries-api-limited

heroku config:set SECRET_KEY="abc123" -a groceries-api-csv
heroku config:set FLASK_ENV="production" -a groceries-api-csv
```

## Deploying

Deploy the source code (where `my_remote` and `my_branch` correspond to the environment you want to deploy to, and the branch you want to deploy, respectively -- see "Deployment Environments" section below for examples):

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
heroku app name: | `groceries-api-limited`
url: | https://groceries-api-limited.herokuapp.com/
git remote name: | `heroku`
git branch name: | `master`

To setup remote address (one-time only):

```sh
heroku git:remote -a groceries-api-limited
# or...
# git remote add heroku https://git.heroku.com/groceries-api-limited.git
```

To deploy:

```sh
git push heroku master
```

### Production (CSV)

Uses a CSV file datastore, supports all operations.

&nbsp; | &nbsp;
--- | ---
heroku app name: | `groceries-api-csv`
url: | https://groceries-api-csv.herokuapp.com/
git remote name: | `heroku-csv`
git branch name: | `csv`

> NOTE: Heroku's ephemeral file system will delete any file not included in the source repository, so attempts to create the `products_production.csv` file won't work when done either manually or during the deployment process. So this file needs to be checked in to the repository for the app to work in production. And this means the file will get overwritten every time there is a deploy.

To setup remote address (one-time only):

```sh
git remote add heroku-csv https://git.heroku.com/groceries-api-csv.git
```

To deploy the "csv" branch:

```sh
git push heroku-csv csv:master
```

Migrate/seed/reset the database as necessary:

```sh
heroku run "python products_api/reset.py"
heroku run "python products_api/seed.py"
```
