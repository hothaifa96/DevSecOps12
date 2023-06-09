import requests
import os

def get_status_code(url):
    response = requests.get(url)
    return response.status_code//100

u = os.environ.get('URL')
print(u)
print(type(u))
u='https://'+u if not u.startswith('https://') else u
print(get_status_code(u))


