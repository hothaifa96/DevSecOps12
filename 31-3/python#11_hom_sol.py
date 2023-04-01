# import json
#
# jsn_str = '{"id": 1,"name": "Leanne Graham","username": true,"email": "Sincere@april.biz"}'
#
# print(jsn_str)
# print(type(jsn_str))
#
# jsn_dic = json.loads(jsn_str)
#
# print(jsn_dic)
# print(type(jsn_dic))
#
# jsn_st2 = json.dumps(jsn_dic)
# print(jsn_st2)
# print(type(jsn_st2))
#
#
# #json ->json.loads() -> dict ->json.dumps()-> json

# 7
# import requests
#
#
# res = requests.get('https://jsonplaceholder.typicode.com/users')
#
# users = res.json() # [{},{}]
#
# for user in users:
#     print( user['email'] )

# 8
# import requests
#
# res = requests.get('https://ips44.onrender.com/ips')
#
# ips = res.json()  # [{ip 1: 123.41.41.4},{}]
#
# for ip in ips:
#     for k, v in ip.items():
#         print(v, end=' ')
#
# print()
# c = 1
# for ip in ips:
#     k = f'ip {c}'
#     print(ip[k], end=' ')
#     c += 1


# 9

# import requests
#
# number = input('enter a number ')
#
# res = requests.get(f'https://jsonplaceholder.typicode.com/photos/{number}')
#
# photo = res.json()
#
# if photo:
#     print(photo)

#

import requests

res = requests.get('https://fruityvice.com/api/fruit/all')

class Nutritions:
    def __init__(self,d):
        self.__dict__=d

class Fruit:
    def __init__(self, d):
        self.__dict__ = d
        self.nutritions = Nutritions(d["nutritions"])

    def __str__(self):
        return f'{self.name}-> sugar {self.nutritions.sugar} '


fruits_dict = res.json()
fruits_objects = []

for fruit in fruits_dict:
    fruit_obj = Fruit(fruit)
    fruits_objects.append(fruit_obj)

# print(fruits_dict)
print([str(x) for x in fruits_objects])
