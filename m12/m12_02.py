# Tutustu avoimeen OpenWeather-säärajapintaan: https://openweathermap.org/api.
# Kirjoita ohjelma, joka kysyy käyttäjältä paikkakunnan nimen ja tulostaa sitä vastaavan säätilan tekstin sekä lämpötilan Celsius-asteina.
# Perehdy rajapinnan dokumentaatioon riittävästi.
# Palvieluun rekisteröityminen on tarpeen, jotta saat rajapintapyynnössä tarvittavan API-avaimen (API key).
# Selvitä myös, miten saat Kelvin-asteet muunnettua Celsius-asteiksi.

import requests
import json

apikey = "2075888ea3393aaa90a63c4e1f765b89"

def weather(city):
    api_location = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=0&appid={apikey}"
    api_location_answer = requests.get(api_location).json()
    location_answer = api_location_answer[0]
    lon = location_answer["lon"]
    lat = location_answer["lat"]
    api_weather = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={apikey}"
    current_weather_response = requests.get(api_weather).json()
    current_temperature = f"{current_weather_response['main']['temp'] - 273.15:.0f}"
    current_weather = []
    for weathers in current_weather_response["weather"]:
        current_weather.append(weathers["main"])
    return current_weather, current_temperature

city = input("City name in English: ")
saa, lampotila = weather(city)
print(f"The weather is {saa[0].lower()} and the temperature {lampotila} Celsius.")

