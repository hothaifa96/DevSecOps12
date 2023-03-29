import requests

res = requests.get('https://jsonplaceholder.typicode.com/users')
print(res.status_code)
users = res.json()  # users = [{},{},{}.....]
print(type(users))
# users = list
# user = dict
# user['name'] = str

for user in users:
    print(user['name'])


class User:
    def __init__(self, d):
        self.__dict__ = d



u1 = User(users[0])
print(u1.name)
