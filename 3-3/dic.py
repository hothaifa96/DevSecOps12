# user1 = {"username": "zahi",
#          "password": 1234}
#
# user2 = dict(username='omer', password=98765)
#
# # print(user2['username'])
# # user2['username'] = 'eli'
# # print(user2.get('username'))
# # print(user2)
#
# # if 'phone' in user2:
# #     print(user2['phone'])
#
# user2['password'] = 'bugatti'
#
# print(user2)
# print(user1)

# point = {'x': 1, 'y': 6, 'color': 'red', 'size': 15}
#
# for k, v in point.items():  # [('x',1),('y',6),('color','red'),()]
#     print(f'{k}  is {v}')
#
# for k in point.keys():
#     print(point[k])
#
# print(point.items())
# print(point.keys())
# print(point.values())


# wpt receive from the user id as key and name as value
# manage to add them to a dict named ids
# declare the dict to be a empty dict
# when the user inserts done stop the process and print the dict

ids = dict()

while True:
    id = input('enter id :')
    if id =='done':
        break
    name = input('enter a name :')
    ids[id] = name

print(ids)

