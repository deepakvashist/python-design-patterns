class MakeMeal:

    def buy_ingredients(self, money):
        if money < self.cost:
            assert 0, "Not enough money to buy ingredients!"

    def prepare(self):
        pass

    def cook(self):
        pass

    def go(self, money):
        self.buy_ingredients(money)
        self.prepare()
        self.cook()


class MakePizza(MakeMeal):

    def __init__(self):
        self.cost = 3

    def prepare(self):
        print("Prepare Pizza - Make the dough and add toppings")

    def cook(self):
        print("Cook Pizza - Cook in the oven on gas mark 8 for 10 minutes")


class MakeCake(MakeMeal):

    def __init__(self):
        self.cost = 2

    def prepare(self):
        print("Prepare Cake - Mix ingredients together and pour into a cake tin")

    def cook(self):
        print("Cook Cake - Bake in the oven on gas mark 6 for 20 minutes")
