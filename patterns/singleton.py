class Singleton:

    __instance = None

    def __new__(cls, value=None):
        if Singleton.__instance is None:
            Singleton.__instance = object.__new__(cls)
        Singleton.__instance.value = value
        return Singleton.__instance


if __name__ == '__main__':
    singleton_a = Singleton()
    singleton_a.value = "Singleton A"
    singleton_b = Singleton()
    singleton_b.value = "Singleton B"

    print('singleton_a.value:', singleton_a.value)
    print('singleton_b.value:', singleton_b.value)
    print("singleton_a == singleton_b:", singleton_a == singleton_b)
