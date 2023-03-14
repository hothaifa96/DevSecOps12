# # 2 def functionname():
#
#
# # def demo(a, b=0, c=0):
# #     return a+b+c
# #
# #
# # demo(a=1, c=3)
# # demo(1, 3)
#
# #5
# def area(b, h):
#     a = b * h / 2
#     return a
#
#
# ar1 = area(6, 8)
# ar2 = area(2, 4)
#
# print(max(ar1, ar2))
#
# def eat():
#     print('eating .....')
# #6
# x = eat()
# print(x)
# 8

#
# import math
# def hekef(radius):
#     hek = math.pi * 2 * radius
#     return hek
#
#
# h1 = hekef(5)
#
# print(h1)

#9
def add(x=0, y=0):
    return x + y


def sub(x=0, y=0):
    return x - y


def mul(x=0, y=0):
    return x * y


def div(x=0, y=0):
    if y == 0:
        print('wake up')
        return 0
    else:
        return x / y


number1 = float(input('please enter a number '))
number2 = float(input('please enter a number '))

print(div(number1, number2))
print(sub(number1, number2))
print(add(number1, number2))
print(mul(number1, number2))
