# # numbers = [1, 2, 3, 4, 1, 2, 2, 2, 1, 17]
# #
# # uniques = {1, 2, 3, 4, 1, 2, 2, 2, 1, 17} # set distinct lists
# #
# # fixed = (1, 2, 3, 4, 1, 2, 2, 2, 1, 17) #tuple(numbers) # fixed  list
# #
# # numbers.append(200)
# #
# # print(numbers)
# # print(uniques)
# # print(fixed)
#
# products = ['shirt', 'shirt', 'jeans', 'jeans', 'jeans', 'jeans', 'allstars']
# products.append('t-shirt')
# category = set(products)
#
# category_list = list(products)
#
# print(products)
# print(category)
#
#
# tuple - set -list
#


users = ('zahi','eli','eido','dvir','gzal')

password = input('enter ypur password')
if password == 'sudo':
    users = list(users)
    users.append('omer')
    users = tuple(users)

print(users)
