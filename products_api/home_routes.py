from flask import Blueprint, current_app, render_template, request

home_routes = Blueprint('home_routes', __name__)

@home_routes.route('/')
def index():
    current_app.logger.info("INDEX")
    return render_template('index.html')

@home_routes.route('/hello')
def hello(name=None):
    current_app.logger.info("HELLO")
    if "name" in request.args:
        name = request.args["name"]
    return render_template('hello.html', name=name)
