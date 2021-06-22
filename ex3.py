import requests,json
r =requests.get('https://restcountries.eu/rest/v2/name/brasil')
brasil = json.loads(r.text)[0]
print(brasil)
