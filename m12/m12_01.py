#Kirjoita ohjelma, joka hakee ja tulostaa satunnaisen Chuck Norris -vitsin käyttäjälle.
# Käytä seuravalla sivulla esiteltävää rajapintaa: https://api.chucknorris.io/.
# Käyttäjälle on näytettävä pelkkä vitsin teksti.

import requests
import json

api = "https://api.chucknorris.io/jokes/random"

vitsi = requests.get(api).json()

print(vitsi["value"])