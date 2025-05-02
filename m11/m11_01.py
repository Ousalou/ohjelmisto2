#Toteuta seuraava luokkahierarkia Python-kielellä: Julkaisu voi olla kirja tai lehti.
# Jokaisella julkaisulla on nimi. Kirjalla on lisäksi kirjoittaja ja sivumäärä, kun taas lehdellä on päätoimittaja.
# Kirjoita luokkiin myös tarvittavat alustajat. Tee aliluokkiin metodi tulosta_tiedot, joka tulostaa kyseisen julkaisun kaikki tiedot.
# Luo pääohjelmassa julkaisut Aku Ankka (päätoimittaja Aki Hyyppä) ja Hytti n:o 6 (kirjailija Rosa Liksom, 200 sivua).
# Tulosta molempien julkaisujen kaikki tiedot toteuttamiesi metodien avulla.

class Julkaisu:
    def __init__(julkaisu, nimi):
        julkaisu.nimi = nimi

class Kirja(Julkaisu):
    def __init__(kirja, nimi, kirjoittaja, sivumaara):
        super().__init__(nimi)
        kirja.sivumaara = sivumaara
        kirja.kirjoittaja = kirjoittaja

class Lehti(Julkaisu):
    def __init__(lehti, nimi, paatoimittaja):
        super().__init__(nimi)
        lehti.paatoimittaja = paatoimittaja

aku_ankka = Lehti("Aku Ankka", "Aki Hyyyppä")
hnro_9 = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

print(aku_ankka.nimi, aku_ankka.paatoimittaja)
print(hnro_9.nimi, hnro_9.kirjoittaja, hnro_9.sivumaara)

