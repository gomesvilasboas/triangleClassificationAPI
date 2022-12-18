from triangleClassificationAPI.model.resquest_handler import RequestHandler
from triangleClassificationAPI.model.operation import Operations
from triangleClassificationAPI.model.data_handler import DataHandler
from triangleClassificationAPI.model.request_schema import request_classification_schema
from flask_expects_json import expects_json
from flask import jsonify, make_response, request, Blueprint

classification_controller_bp = Blueprint('classificationController', __name__)


@classification_controller_bp.route('/', methods=['GET'])
def root():
    data = {
        'message': 'Server is working properly.',
        'code': 'SUCCESS'
    }
    return make_response(jsonify(data), 201)


@classification_controller_bp.route('/classify', methods=['POST'])
@expects_json(request_classification_schema)
def classify():
    RequestHandler.validate_content_type(request.content_type)
    x, y, z = DataHandler.get_sides_length(request.json)
    DataHandler.is_a_valid_triangle(x, y, z)
    classification = Operations.triangle_classification(x, y, z)
    response = {
        'class': classification,
        'code': 'SUCCESS'
    }
    return make_response(jsonify(response), 200)
