# def get_number(text):
#     '''
#     :param text: number as a text with dollar sign
#     :return: int the number from the text
#     '''
#     number = int(text[1:])
#     return number
#
#
# def avg(*args):  # [1,2,3,4,5,6,7,8] [[1,2,4]]
#     sum = 0
#     for i in args:
#         if type(i) == list:
#             for j in i:
#                 sum += j
#         else:
#             sum += i
#     return sum // len(args)
#
#
# # '$15' -> 15
# # '$199' -> 199
#
# # price1 = '$1'
# # price2 = '$199'
# # price3 = '$1780000'
# #
# # price1 = get_number(price1)
# # price2 = get_number(price2)
# # price3 = get_number(price3)
# # print(price1)
# # print(price2)
# # print(price3)
# # print(avg(price3,price2,price1))
#
# prices = ['$2000', '$350', '$500', '$798', '$22']
# new_prices = []
#
# for price in prices:
#     temp = get_number(price)
#     new_prices.append(temp)
#
# avg1 = avg(new_prices)
# print(prices)
# print(new_prices)
# print(avg1)
#
# x = 4
# y = 6
# z = 10
#
# print(avg(x, y, z, 5, 11, 15))
# print(avg([1, 3, 4]))


# def render(*args):
#     for text in args:
#         print(f'{text} -> {text[::-1]}')
#
#
# render('shawarma', 'pizza', 'passta', 'dad')

# x = 'hothaifa'
#
# def online(x):
#     x = 6
#     print(x)
#
#
# online()
# print(x)

