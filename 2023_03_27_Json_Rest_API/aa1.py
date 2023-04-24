import requests

url = "https://www.party-games.com/api/random"
url = "http://www.boredapi.com/api/activity?participants=8"

data = requests.get(url).json()
print(data)
print(data["activity"])
