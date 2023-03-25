# number = int(input('enter a number :'))
# div = number
#
# while div > 0:
#     if number % div == 0:
#         print(f'{div} * {number//div}')
#     div -= 1
#
#
# # 12
# #
# # 2 * 6
# # 4 * 3
# # 1 * 12
#
#
#
#
#
#
#


def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        print('fizzbuzz')
    elif number % 3 == 0:
        print('fizz')
    elif number % 5 == 0:
        print('buzz')
    else:
        print(number)


def fizzbuzz(number):
    str = ''
    if number % 3 == 0:
        str += 'fizz'
    if number % 5 == 0:
        str += 'buzz'
    if str == '':
        str = number

    return str


print(fizzbuzz(7))
