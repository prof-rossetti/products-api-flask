# Deployer's Guide

## Prerequisites

Install the heroku command-line utility (perhaps via `brew install heroku`), then login to your heroku account with `heroku login`.

### Initializing a Heroku Server

Then create a new app server:

```sh
heroku create # then note your application's name
```

## Deploying

```sh
git push heroku my_branch:master
```
