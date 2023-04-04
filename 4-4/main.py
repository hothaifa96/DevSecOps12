import os
import requests

# os.mkdir('hodi1')
# os.chdir('hodi1')

# os.chmod()
# os.system('echo hello >> file2.txt')
# name = input('enter dir name')
# os.system(f'mkdir {name}')

# --------- automation exmple ----------
# res = requests.get('https://fruityvice.com/api/fruit/all')
#
# fruits = res.json() #''-[{},]
#
# for fruit in fruits:
#     os.system(f'mkdir {fruit["name"]}')
#     os.system(f'cd {fruit["name"]} && echo {fruit} >> {fruit["name"]}.json')
#

url = 'https://github.com/harpazofek/Tic-Tac-Toe'
os.system(f'git clone {url}')
dir_name= url.split('/')[-1]
os.system(f'cd {dir_name} && python3 main.py')



