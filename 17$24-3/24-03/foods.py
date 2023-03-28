class McFlurry:
    def __init__(self, calories, flavor, price=15.90):
        self.__calories = calories
        self.__flavor = flavor
        self.__price = price

    @property  # GETTER
    def calories(self):
        return self.__calories

    @calories.setter  # SETTER
    def calories(self, new_cal):
        if new_cal > self.__calories:
            self.__calories = new_cal


class Burger:
    def __init__(self, calories, topping, price):
        self.__calories = calories
        self.topping = topping
        self.__price = price

    @property
    def calories(self):
        return self.__calories()

    @calories.setter
    def calories(self, new_calories):
        if new_calories > 0:
            self.__calories = new_calories

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        self.__price = new_price if new_price % 2 == 0 else new_price + 1

    def __str__(self):
        return f'Burger {self.topping}'


ice_dvir = McFlurry(500, 'carmel')

print(ice_dvir.calories)
ice_dvir.calories = 1500
print(ice_dvir.calories)
