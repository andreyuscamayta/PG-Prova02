import requests,json
r =requests.get('https://jsonplaceholder.typicode.com/users')
usuarios = json.loads(r.text)
print(usuarios)
