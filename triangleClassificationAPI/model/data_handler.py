from flask import abort


class DataHandler:
    @staticmethod
    def get_sides_length(request):
        try:
            x = float(request['x'])
            y = float(request['y'])
            z = float(request['z'])
            return x, y, z
        except Exception as ex:
            abort(400, description='Data conversion error.')

    @staticmethod
    def is_a_valid_triangle(x, y, z):
        if (x + y <= z) or (x + z <= y) or (y + z <= x):
            abort(400, description='It is not a triangle')