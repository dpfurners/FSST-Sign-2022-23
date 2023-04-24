import base64
import os

import requests


GEOCODING_URL = "https://api.openweathermap.org/geo/1.0/direct"
WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"


def load_key_from_env(env_key: str = "WEATHER_API_KEY", key: str | None = None):
    if key is None:
        key = os.environ.get(env_key)
    return key


def request(url: str, key: str | None = None, **params) -> dict:
    key = load_key_from_env(key=key)
    params = {**params, "appid": key}
    req = requests.get(url, params=params)
    if req.status_code != 200:
        raise ValueError(req.json()["message"])
    return req.json()


def resolve_city_data(city: str, key: str | None = None, lang: bool = False) -> tuple[float, float] | list[str]:
    key = load_key_from_env(key=key)
    lang_lat = request(GEOCODING_URL, key, q=city)
    if lang:
        try:
            ind = list(lang_lat[0]["local_names"]).index("en")
            local_names_values = list(lang_lat[0]["local_names"].values())
            return local_names_values[ind:] + local_names_values[:ind]
        except KeyError:
            return [lang_lat[0]["name"]]
        except IndexError:
            raise ValueError("City not found.")
    # Last element is the most accurate (from what I found out)
    lat = lang_lat[len(lang_lat)-1]["lat"]
    lon = lang_lat[len(lang_lat)-1]["lon"]
    return lat, lon


def resolve_city_weather(city: str, key: str | None = None) -> dict:
    key = load_key_from_env(key=key)
    lat, lon = resolve_city_data(city, key)
    data = request(WEATHER_URL, key, lat=lat, lon=lon, units="metric")
    return data


def get_weather_icon(icon_id: str) -> bytes:
    url = f'https://openweathermap.org/img/wn/{icon_id}.png'
    response = requests.get(url, stream=True)
    return base64.encodebytes(response.raw.read())
