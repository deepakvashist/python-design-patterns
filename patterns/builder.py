class Car:

    def __init__(self):
        self.__wheels = []
        self.__engine = None
        self.__body = None

    def set_body(self, body):
        self.__body = body

    def attach_wheels(self, wheel):
        self.__wheels.append(wheel)

    def set_engine(self, engine):
        self.__engine = engine

    def specification(self):
        print("Body:", self.__body.shape)
        print("Engine horsepower:", self.__engine.horsepower)
        print("Tire size:", self.__wheels[0].size)


class Wheel:
    size = None


class Engine:
    horsepower = None


class Body:
    shape = None


class Director:
    __builder = None

    def set_builder(self, builder):
        self.__builder = builder

    def get_car(self):
        car = Car()

        # First goes the body
        body = self.__builder.get_body()
        car.set_body(body)

        # Then engine
        engine = self.__builder.get_engine()
        car.set_engine(engine)

        # And four wheels
        for i in range(1, 5):
            wheel = self.__builder.get_wheel()
            car.attach_wheels(wheel)

        return car


class BuilderInterface:

    def get_wheel(self):
        pass

    def get_engine(self):
        pass

    def get_body(self):
        pass


class JeepBuilder(BuilderInterface):

    def get_wheel(self):
        wheel = Wheel()
        wheel.size = 22
        return wheel

    def get_engine(self):
        engine = Engine()
        engine.horsepower = 400
        return engine

    def get_body(self):
        body = Body()
        body.shape = 'SUV'
        return body


class NissanBuilder(BuilderInterface):

    def get_wheel(self):
        wheel = Wheel()
        wheel.size = 16
        return wheel

    def get_engine(self):
        engine = Engine()
        engine.horsepower = 100
        return engine

    def get_body(self):
        body = Body()
        body.shape = 'Hatchback'
        return body


if __name__ == '__main__':
    director = Director()
    director.set_builder(JeepBuilder())
    car = director.get_car()
    car.specification()
