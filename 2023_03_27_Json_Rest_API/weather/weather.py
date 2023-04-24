import requests

key = "dsöjflakäsdklfjghblöopidisfö"

url_lang_lat = f"http://api.openweathermap.org/geo/1.0/direct?q=Austria&limit=1&appid={key}"
lang_lat = requests.get(url_lang_lat).json()
print(lang_lat)
lat = lang_lat[0]["lat"]
lon = lang_lat[0]["lon"]

url_weather = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}"

data = requests.get(url_weather).json()

print(data)
