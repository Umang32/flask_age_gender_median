import requests


url = "https://api.npoint.io/adc85df890077790d3c9"
response = requests.get(url)
response = response.json()
print(response[0]["title"])