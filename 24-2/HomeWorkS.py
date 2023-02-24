# z = int(input('give me something '))
# z = float(input('give me something '))
#
#
#name = 'yoni'
#
# b = 'yo' in name

# if cond1 and cond3:
#     #true block
# elif cond2 :
#     # true block
# else:
#     #false block
# if 1 == 1:
#     print('hello')
#     print('hhhh gotim')
# print('tzahi')

#6
# number = int(input('please enter a number :'))
# number2 = int(input('please enter a number :'))
#
# if number < number2:
#     print(f'and the min is {number}')
# elif number == number2:
#     print('go get some coffee and then enter a number ')
# else:
#     print(f'and the min is {number2}')
#
# x = int(input('please enter a number :'))
# y = int(input('please enter a number :'))
# z = int(input('please enter a number :'))
#
# if x > y and x > z:
#     print(x)
# elif y > z:
#     print(y)
# else:
#     print(z)

#7

# inp = int(input('enter a number '))
#
# print(inp % 3 == 0)

#8

# month = input('enter the month:')
#
# months_with_31 = '3 5 7 8 10 12'
# months_with_30 = '4 9 11 6'
#
# if month == '2':
#     year = int(input('enter year :'))
#     if year % 400 == 0 or (year % 4 ==0 and year % 100 != 0):
#         print(f'29 days in {month}')
#     else:
#         print(f'28 days in {month}')
# elif month in months_with_31:
#     print(f'31 days in {month}')
# elif months_with_30:
#     print(f'30 days in {month}')
# else:
#     print('invalid input .....')


#10
# day = int(input('enter the day number'))
# day %= 7
#
# if day == 1:
#     print('sunday')
# elif day == 2:
#     print('monday')
# elif day == 3:
#     print('tuesday')
# elif day == 4:
#     print('wednesday')
# elif day == 5:
#     print('thursday')
# elif day == 6:
#     print('friday')
# else:
#     print('saturday')

# formula = input('enter a math exr like 5 * 2 = 10 : ')
# '44 + 3 = 6'
# sp = formula.find(' ') # 2
# x = int(formula[:sp]) #44
# formula = formula[sp+1:] # '+ 3 = 6'
#
#
# sp = formula.find(' ') # 1
# formula =formula[sp+1:] # '3 = 6'
#
# sp = formula.find(' ') # 1
# y = int(formula[:sp])  # 3
# formula = formula[sp+1:] # '= 6'
#
# sp = formula.find(' ') #  1
# guess = int(formula[sp+1:])  #6
#
#  # 4 int
# ans = x + y
# print(ans == guess)