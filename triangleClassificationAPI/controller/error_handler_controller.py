from flask import jsonify, Blueprint
from werkzeug.exceptions import HTTPException

error_handler_request_bp = Blueprint('error_handler_request', __name__)


@error_handler_request_bp.app_errorhandler(HTTPException)
def handle_error(e):
    code = 500
    if isinstance(e, HTTPException):
        code = e.code
    return jsonify(error=str(e)), code
