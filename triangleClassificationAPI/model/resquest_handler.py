from flask import abort


class RequestHandler:
    @staticmethod
    def validate_content_type(content_type):
        if content_type != 'application/json':
            abort(415, description='Unsupported content type')