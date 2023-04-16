import requests

# high_sugar = open('hight_sugar.txt', 'w')

# with open('high_sugar.txt','w') as high_sugar:
#     with open('low_sugar.txt','w') as low_sugar:
#         fruits = requests.get('https://fruityvice.com/api/fruit/all').json()
#         print(type(fruits[0]))
#
#         for fruit in fruits:
#             if fruit['nutritions']['sugar'] > 7:
#                 high_sugar.write(fruit['name']+'\n')
#             else:
#                 low_sugar.write(fruit['name']+'\n')
#
# file = open('hight_sugar.txt','r')
# print(file.read())
# # high_sugar.writelines([fruit['name'] for fruit in fruits if fruit['nutritions']['sugar'] > 7])
# # low_sugar.writelines([fruit['name'] for fruit in fruits if fruit['nutritions']['sugar'] <= 7])


