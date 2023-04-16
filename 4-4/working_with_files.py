import requests
# how to write to a file
# open(filepath , mode)
# file = open('name.txt', 'a')
# #
# # while True:
# #     name = input('please enter a name')
# #     if name.lower() == 'q':
# #         break
# #     else:
# #         file.write(name+'\n')
# #
# # print('thx')
#
# res = requests.get('https://jsonplaceholder.typicode.com/users')
#
# users = res.json()
#
# for user in users:
#     file.write(user['name']+'\n')

n_file = open('name.txt','a+')

# print(n_file.read())
#
# print('---------')
# # print(n_file.tell()) # tell where the curser
# n_file.seek(0) # change the location of the curser
# print(n_file.read())

# n_file.seek(30)
# print(n_file.read(60))
# print(n_file.tell())

n_file.seek(0)
lines = n_file.readlines()
print(lines)
for line in lines:
    print(f'{line[:-1]} - ' ,end='')

# file = open(file,mode)
# file.write()


