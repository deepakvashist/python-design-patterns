class EuropeanSocketinterface:

    def voltage(self):
        pass

    def live(self):
        pass

    def neutral(self):
        pass

    def earth(self):
        pass


class USASocketinterface:

    def voltage(self):
        pass

    def live(self):
        pass

    def neutral(self):
        pass


class EuropeanSocket(EuropeanSocketinterface):

    def voltage(self):
        return 230

    def live(self):
        return 1

    def neutral(self):
        return -1

    def earth(self):
        return 0


class AmericanKettle:

    __power = None

    def __init__(self, power):
        self.__power = power

    def boil(self):
        if self.__power.voltage() > 110:
            print("Kettle on fire!")
        else:
            if self.__power.live() == 1 and self.__power.neutral() == -1:
                print("Coffe time!")
            else:
                print("No power.")


class Adapter(USASocketinterface):

    __socket = None

    def __init__(self, socket):
        self.__socket = socket

    def voltage(self):
        return 110

    def live(self):
        return self.__socket.live()

    def neutral(self):
        return self.__socket.neutral()


if __name__ == '__main__':
    socket = EuropeanSocket()

    kettle = AmericanKettle(socket)
    kettle.boil()

    adapter = Adapter(socket)
    kettle = AmericanKettle(adapter)
    kettle.boil()
