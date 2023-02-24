# short handed if
# x = int(input('enter a number'))
#
# name = 'zahi' if x > 5 else 'dvir'
# #true block  if  cond  else   false block
#
# print(name)
#

# list

# name = [1, 'hello', 3, 5, True, 88.6, 33,[222,55]]

# cars = ['audi a7', 'lada' , 'audi rs7', 'audi rs8' , 'supra', 'cupra']
#
# print(cars)

# print(cars.count('audi'))
# l = cars.pop()
# print(l)
# cars.append('yaris')
# cars.remove(cars)
# cars.clear() # []
# print(cars.index('supra'))
# cars[1] = 'mazda cx-5'
# cars.insert(0, 'volvo')
# print(len(cars))

# q = 'bug bsystem shel hamester'
#
# qlist = q.split('s')
# print(qlist)


# numbers = [1,-2,3,-4,5,-6,7,-8,9,-10]
#
# print(numbers)
# # numbers.sort()
# # numbers.reverse()
# print(list(reversed(numbers)))
# print(numbers)

# sen = 'joey doesnt share food '
# list1 = sen.split()
# "['joey', 'doesnt', 'share', 'food']"
# print(sen)
# print(list1)
# print(str(list1))
#
# print(sen[0])
# print(list1[0])


# numbers =list(range(0,51,10))
# print(numbers)

#loops

# for i in range(11):   # - 0,1,2,3,4,5,6,7-
#     # print(f'even {i}' if i % 2 ==0 else f'odd {i}')
#     if i % 2 ==0:
#         print(f'even {i}')
#     else:
#         print(f'odd {i}')

# limit = int(input('enter a number bigger than 0 :'))
#
# for i in range(limit):
#     print(f'hello {i}')

# write a python program to sum all the number from 0
# to the user input with the user input using for loop

# limit = int(input('enter a number : '))
# sum = 0
# for n in range(limit+1):
#     sum += n
# print(f'the sum is : {sum} ')

name2 = 'arik vaserman'
names = ['arik','vaserman','rozan','hodi','aviv','israel','dvir','omer','shlomo']

for name in names:
    if 'a' in name:
        break
    print(name.upper())
else:
    print('else')
print('thats it for today')
