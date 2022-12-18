class Operations:
    @staticmethod
    def triangle_classification(x, y, z):
        if x == y == z:
            return "Equilateral triangle"
        if x == y or y == z or z == x:
            return "Isosceles triangle"
        return "Scalene triangle"

