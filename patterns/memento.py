import copy


class Memento:

    def __init__(self, data):
        for attribute in vars(data):
            setattr(self, attribute, copy.deepcopy(getattr(data, attribute)))


class Undoable:

    def __init__(self):
        self.__last = None

    def save(self):
        self.__last = Memento(self)

    def undo(self):
        for attribute in vars(self):
            setattr(self, attribute, getattr(self.__last, attribute))


class Data(Undoable):

    def __init__(self):
        super().__init__()
        self.numbers = []


if __name__ == '__main__':
    data = Data()
    repeats = 10

    for i in range(repeats):
        data.save()
        data.numbers.append(i)

    for i in range(repeats):
        data.undo()
        print(data.numbers)
