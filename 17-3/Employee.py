import random


class Employee:
    def __init__(self, name, age):
        # constructor
        self.name = name
        self.age = age

    def work(self):
        print('working ...........')

    def make_coffee(self):
        print('strong black coffee with no sugar .....')

    def tell_me_your_name(self):
        print(f'my name is {self.name}')

    def __str__(self):
        return f'name: {self.name} age {self.age}'


# israel = Employee()
#
# israel.work()
#
# israel.make_coffee()
# israel.make_coffee()
# israel.make_coffee()
# israel.make_coffee()
#
# rafi = int(2)
# print( isinstance(israel,Employee) )
omer = Employee('omer', 18)
zahi = Employee('zahi', 50)
print(omer)
print(f'omer -> {omer.name}')
print(f'zahi -> {zahi.name} age -> {zahi.age}')

omer.tell_me_your_name()
zahi.tell_me_your_name()

