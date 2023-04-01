import requests

res = requests.get('https://www.google.com')

print(res)

print(res.status_code)  # int status code
# print(res.text) #text - body of the response
# print(res.content) #like text but in one line
# print(res.url)
# print(res.headers)


if 200 <= res.status_code < 300:
    print('success')
else:
    print('Error')
