class ComputerState:
    name = 'state'
    allowed = []

    def switch(self, state):
        if state.name in self.allowed:
            print("Current: {} => switched to new state {}"
                  .format(self, state.name))
        else:
            print("Current: {} => switching to {} not possible"
                  .format(self, state.name))

    def __str__(self):
        return self.name


class Off(ComputerState):
    name = 'off'
    allowed = ['on', ]


class On(ComputerState):
    name = 'on'
    allowed = ['off', 'suspend', 'hibernated']


class Suspend(ComputerState):
    name = 'suspend'
    allowed = ['on', ]


class Hiberneate(ComputerState):
    name = 'hibernate'
    allowed = ['on', ]


class Computer:

    def __init__(self):
        self.state = Off()

    def change(self, state):
        self.state.switch(state)


if __name__ == '__main__':
    computer = Computer()
    computer.change(On)
    computer.change(Off)
