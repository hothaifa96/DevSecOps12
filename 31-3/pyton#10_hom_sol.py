# PYTHON #10

# 1 decorator @ -> @prop.getter @ name.setter @classmethod

# 2 validation - getter to receive the private value and setter to override it

# 3 def get_name(self):
# c1.get_name()
# @prop
# c1.name =


# help -python doc (search)
# dir -> prints all the methods in class as one list

# class Hodi:
#     def hello(self):
#         pass
#     def mas(self):
#         pass
#
# print(dir(Hodi))

# 6
# class A:
#     pass
#
#
# class B(A):
#     pass

# 7
# class A:
#     def hello(self):
#         print('a')
#
#
# class B(A):
#     def hello(self):
#         print('b')
#
#
# class C(B):
#     def hello(self):
#         print('c')
#
#
# b1 = B()
# b1.hello()

# 8
# polymorphism - many forms
# zahi -> baby -> eat : 10
# zahi -> kid -> eat : 15
# zahi -> teen -> eat : 4
# zahi -> adult -> eat : 16
# zahi -> lover -> eat : 480
# zahi -> husband -> eat : 5
# zahi -> dad -
# zahi -> grandpa -> eat : 190
# zahi -> employee -> eat : 45
# zahi -> manager -> eat : 60

# 10
# super -> dad class


# class Shape:
#     def __init__(self, color):
#         self.color = color
#
#     def __str__(self):
#         return f'{self.color}'
#
#
# class Circle(Shape):
#     def __init__(self, color, r):
#         # super().__init__(self, color)
#         Shape.__init__(self, color)
#         self.r = r
#
#     def __str__(self):
#         return super().__str__() + f'{self.r}'
#
# s1 = Shape('red')
# print(s1)

class Shape:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'name:{self.name}'


class FourSides(Shape):
    def __init__(self, name, a, b, c, d):
        Shape.__init__(self, name)
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def get_hekef(self):
        return self.a + self.b + self.c + self.d

    def __str__(self):
        return super().__str__() + f' a:{self.a} b:{self.b} ' \
                                   f'c:{self.c} d:{self.d} hekef:{self.get_hekef()} '


class Rectangle(FourSides):
    def __init__(self, name, x, y):
        FourSides.__init__(self, name, x, y, x, y)

    def get_Area(self):
        return self.a * self.b
    def __str__(self):
        return super().__str__() + f'area :{self.get_Area()}'

class Square(Rectangle):
    def __init__(self,name , z ):
        Rectangle.__init__(self,name,z,z)

    def __str__(self):
        return super().__str__()


f1 = FourSides('sponge bob', 4, 4, 4, 4)
f2 = Rectangle('name', 5, 4)
f3 = Square('peso',9)

print(f1)
print(f2)
print(f3)