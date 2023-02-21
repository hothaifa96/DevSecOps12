import math

# print(math.e)
# print(math.pi)
# print(math.pow(16,-4)) # 2**4
# print(math.sqrt(4)) # 2**4
# print(math.floor(3.9))
# print(math.ceil(3.00001))
# print(round(5.99))

# casting
# x = 1
# y = '1'
# # print(y+x)
# print(type(y))
# y = int(y)
# print(type(y))
# print(y+x)

# x = '-44.66'
# t = x[1:3] # -> '44'
# z = int(t)
# print(z)
# # bool -> True -> 1 2  4 3 'zero' 'fasle' 4.4
# # bool -> False -> 0 '' 0.0 None
#

# x = int(input('please enter a number : '))
#
# print(type(x))

# ask the user to insert 2 numbers and print the diff between them

# write a program to receive the number of pizzas we order
# and print the number of slices  each pizza is 8 slices

# etgar ask the  user to enter the number of eaters (his friends)
# calc how many slices each friend will get and how many leftovers
#
pizzas = int(input('enter the number of pizza\'s:  '))
friends = int(input('how many friends you have right now : '))

slices = pizzas * 8
slices_per_person = slices // friends
leftovers = slices % friends

print(f'you have ordered {slices} slices and each one will '
      f'get {slices_per_person} the leftovers : {leftovers}')
# print('you have orders',slices)
