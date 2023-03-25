import math


class Circle:
    def __init__(self, r):
        self.r = r

    def calc_area(self):
        return math.pi * self.r ** 2

    def calc_hekef(self):
        return math.pi * self.r * 2

    def __str__(self):
        return f'Circle -> radius : {self.r}'


c1 = Circle(5)
c2 = Circle(8)

print(c1)
print(c2)

print(c1.calc_area())
print(c2.calc_area())

print(f'max area in -> {c1 if c1.calc_area() > c2.calc_area() else c2}')
