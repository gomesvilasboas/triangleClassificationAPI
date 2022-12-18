from flask import jsonify, make_response, Blueprint

monitoring_controller_bp = Blueprint('monitoring_controller', __name__)


@monitoring_controller_bp.route('/healthcheck', methods=['GET'])
def health_check():
    health_check_message = {
        'message': 'Server is up and running properly',
        'code': 'SUCCESS'
    }
    return make_response(jsonify(health_check_message)), 200
