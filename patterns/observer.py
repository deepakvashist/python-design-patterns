class Observable:

    def __init__(self):
        self.observers = []

    def register(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)

    def unregister(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def unregister_all(self):
        if self.observers:
            del self.observers[:]

    def update_observers(self, *args, **kwargs):
        for observer in self.observers:
            observer.update(*args, **kwargs)


class Observer:

    def update(self, *args, **kwargs):
        pass


class AmericanStockMarket(Observer):

    def update(self, *args, **kwargs):
        print("American stock market received: {}\n{}".format(args, **kwargs))


class EuropeanStockMarket(Observer):

    def update(self, *args, **kwargs):
        print("European stock market received: {}\n{}".format(args, **kwargs))


if __name__ == '__main__':
    company = Observable()
    american_observer = AmericanStockMarket()
    company.register(american_observer)
    european_observer = EuropeanStockMarket()
    company.register(european_observer)

    company.update_observers('note', msg="Important note")
