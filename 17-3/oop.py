# class Laptop:
#     def power_on(self):
#         print('starting the computer ......')
#
#     def power_off(self):
#         print('shutting down ......')
#
#
# lenovo = Laptop()
# lenovo.power_on()
#
#
# hp = Laptop()
# hp.power_on()
#
#
# print(lenovo)


class Car:
    def go(self):
        print('Going ...')

    def breake(self):
        print('Stopping .....')

    def fill_il(self, lt):
        print(f'filling {lt}-lt  of gas')


volvo = Car()

print(type(volvo))
if isinstance(volvo, Car):
    print('yes volvo is a Car')

volvo.go()
honda = Car()

honda.breake()
honda.fill_il(66)

