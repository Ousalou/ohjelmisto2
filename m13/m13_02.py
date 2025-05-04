# Toteuta taustapalvelu, joka palauttaa annettua lentokentän ICAO-koodia vastaavan lentokentän nimen ja kaupungin JSON-muodossa.
# Tiedot haetaan opintojaksolla käytetystä lentokenttätietokannasta.
# Esimerkiksi EFHK-koodia vastaava GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/kenttä/EFHK.
# Vastauksen on oltava muodossa: {"ICAO":"EFHK", "Name":"Helsinki Vantaa Airport", "Municipality":"Helsinki"}.

from flask import Flask, request, jsonify
import mysql.connector

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port= 3306,
    database='flight_game',
    user='keltanokat',
    password='lentopeli',
    autocommit=True,
    collation='utf8mb3_general_ci'

)

app = Flask(__name__)

@app.route('/kenttä/<string:icao>')
def sql(icao):
    name_sql = f"select name from airport where ident = '{icao}';"
    cursor = yhteys.cursor()
    cursor.execute(name_sql)
    name = cursor.fetchone()
    #city_sql = f"select municipality from airport where ident = '{icao}';"
    #cursor.execute(city_sql)
    #city = cursor.fetchone()
    #cursor.close()
    vastaus = {
        'ICAO': icao,
        'Name': name[0],
      #  'Municipality': city[0]                    #muokattu flight game (peliä varten) ei sisällä tätä tietoa :(
    }
    return jsonify(vastaus)

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)