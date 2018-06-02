from flask import Blueprint, jsonify

error_handlers = Blueprint('error_handlers', __name__)

@error_handlers.errorhandler(400)
def bad_request(message="Not Found"):
    response = jsonify({"status": 400, "message": message})
    response.status_code = 400
    return response
