# Toteuta Flask-taustapalvelu, joka ilmoittaa, onko parametrina saatu luku alkuluku vai ei.
# Hyödynnä toteutuksessa aiempaa tehtävää, jossa alkuluvun testaus tehtiin.
# Esimerkiksi lukua 31 vastaava GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/alkuluku/31.
# Vastauksen on oltava muodossa: {"Number":31, "isPrime":true}.
import requests
from flask import Flask, request, jsonify
import math
app = Flask(__name__)

def alkuluku(number):
    nelio_juuri = int(math.sqrt(number))
    for i in range (2, nelio_juuri + 1):
       if number % i == 0:
        return False
    return True

@app.route('/alkuluku/<int:number>')
def tarkista_alkuluku(number):
    tulos = {
        "Number": number,
        "isPrime": alkuluku(number)
    }
    return jsonify(tulos)

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)