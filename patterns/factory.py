class ShapeInterface:

    def draw(self):
        pass


class Circle(ShapeInterface):

    def draw(self):
        print('Circle.draw')


class Square(ShapeInterface):

    def draw(self):
        print('Square.draw')


class ShapeFactory:

    @staticmethod
    def get_shape(shape_type):
        if shape_type == 'circle':
            return Circle()
        if shape_type == 'square':
            return Square()
        assert 0, "Could not find shape {}".format(shape_type)
