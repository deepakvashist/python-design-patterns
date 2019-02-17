# Abstract shape classes


class Shape2DInterface:

    def draw(self):
        pass


class Shape3DInterface:

    def build(self):
        pass


# Concrete shape classes


class Circle(Shape2DInterface):

    def draw(self):
        print('Circle.draw')


class Square(Shape2DInterface):

    def draw(self):
        print('Square.draw')


class Sphere(Shape3DInterface):

    def build(self):
        print('Sphere.build')


class Cube(Shape3DInterface):

    def build(self):
        print('Cube.build')


# Abstract shape factory


class ShapeFactoryInterface:

    def get_shape(sides):
        pass


# Concrete shape factory


class Shape2DFactory(ShapeFactoryInterface):

    @staticmethod
    def get_shape(sides):
        if sides == 1:
            return Circle()
        if sides == 4:
            return Square()
        assert 0, "Bad 2D shape creation: Shape not defined for {} sides" \
            .format(sides)


class Shape3DFactory(ShapeFactoryInterface):

    @staticmethod
    def get_shape(sides):
        if sides == 1:
            return Sphere()
        if sides == 6:
            return Cube()
        assert 0, "Bad 3D shape creation: Shape not defined for {} sides" \
            .format(sides)
