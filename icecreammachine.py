#  https://www.testdome.com/d/python-interview-questions/9


class IceCreamMachine:

    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings

    def scoops(self):
        final = []
        for ing in self.ingredients:
            for top in self.toppings:
                ml = [ing, top]
                final.append(ml)

        return final


machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"])
print(machine.scoops())  # should print[['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]