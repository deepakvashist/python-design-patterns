class Borg:

    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state


if __name__ == '__main__':
    borg_a = Borg()
    borg_b = Borg()
    borg_c = Borg()

    borg_a.first_name = 'Deepak'
    borg_b.last_name = 'Vashist'
    borg_c.age = 21

    print('borg_a.age:', borg_a.age)
    print('borg_b.first_name:', borg_a.first_name)
    print('borg_c.last_name:', borg_a.age)
