import requests

url = 'https://api.github.com/users/kennethreitz/starred'
w_json = requests.get(url).json()
name = w_json
print(name['name'])