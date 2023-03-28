class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print('making sound')

    def breathe(self):
        print('breathing ,,,,,,')

    def __str__(self):
        return f'{self.name} {self.age}'
class Dog(Animal):
    def __init__(self, name, age, fav_food):
        Animal.__init__(self, name, age)
        self.fav_food = fav_food

    def make_sound(self):
        print('wrouph wrouph ')

    def play(self):
        print('playingg . . . . . ')

    def __str__(self):
        return super().__str__() + f' {self.fav_food}'
# DRY -> dont repeat yourself
class Cat(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, name, age)

    def jump(self):
        print('jumpinggggggg ')
# d1 = Dog('gibour', 17, 'bonzo')
# d2 = Dog('gibour', 17, 'bonzo')
# d1.make_sound()
# d2.make_sound()
#
# c1 = Cat('hatoul', 3)
# #
# # print(isinstance(d1, Dog))
# # print(isinstance(d1, Animal))
# # print(isinstance(d1, Cat))
# #
# # d1.breathe()
# # print(d1.name)
# # print(c1.name)
# # c1.breathe()
#
# d1.make_sound()
# c1.make_sound()
# print(d1)


d1 = Dog('kiwi', 2, 'bonzo')
d2 = Dog('hulk', 3, 'bonzo')
c1 = Cat('Puscho', 66)

animals = [d1, d2, c1]

for animal in animals:
    animal.make_sound()
    animal.breathe()
