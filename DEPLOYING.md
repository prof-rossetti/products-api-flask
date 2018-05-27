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
```

## Deploying

```sh
git push heroku my_branch:master
```
