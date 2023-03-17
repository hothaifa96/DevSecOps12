class Laptop:
    def power_on(self):
        print('starting the computer ......')

    def power_off(self):
        print('shutting down ......')


lenovo = Laptop()
lenovo.power_on()


hp = Laptop()
hp.power_on()


print(lenovo)
print(hp)