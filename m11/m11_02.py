#Kirjoita aiemmin laatimallesi Auto-luokalle aliluokat Sähköauto ja Polttomoottoriauto.
# Sähköautolla on ominaisuutena akkukapasiteetti kilowattitunteina. Polttomoottoriauton ominaisuutena on bensatankin koko litroina.
# Kirjoita aliluokille alustajat. Esimerkiksi sähköauton alustaja saa parametreinaan rekisteritunnuksen, huippunopeuden ja akkukapasiteetin.
# Se kutsuu yliluokan alustajaa kahden ensin mainitun asettamiseksi sekä asettaa oman kapasiteettinsa.
# Kirjoita pääohjelma, jossa luot yhden sähköauton (ABC-15, 180 km/h, 52.5 kWh) ja yhden polttomoottoriauton (ACD-123, 165 km/h, 32.3 l).
# Aseta kummallekin autolle haluamasi nopeus, käske autoja ajamaan kolmen tunnin verran ja tulosta autojen matkamittarilukemat.

import random

class Auto:
    def __init__(auto, rekisteritunnus, max_nopeus, tasa_nopeus):
        auto.rekisteritunnus = rekisteritunnus
        auto.max_nopeus = max_nopeus
        auto.tasa_nopeus = tasa_nopeus
        auto.current_nopeus = tasa_nopeus
        auto.current_matka = 0

    def add_matka(auto):
        auto.current_matka = auto.current_matka + auto.current_nopeus

class Sahko(Auto):
    def __init__(auto, rekisteritunnus, max_nopeus, tasa_nopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, max_nopeus, tasa_nopeus)
        auto.akkukapasiteetti = akkukapasiteetti

class Polttomoottori(Auto):
    def __init__(auto, rekisteritunnus, max_nopeus, tasa_nopeus, bensa_tilavuus):
        super().__init__(rekisteritunnus, max_nopeus, tasa_nopeus)
        auto.bensa_tilavuus = bensa_tilavuus

class Kilpailu:
    def __init__(kisa, autot):
        kisa.autot = autot

    def tunti_kuluu(kisa):
        for i in range (0, len(kisa.autot)):
            print(f"\nAUTO {kisa.autot[i].rekisteritunnus}\n-------------")
            kisa.autot[i].add_matka()
            print(f"Tämänhetkinen kuljettu matka autolla {kisa.autot[i].rekisteritunnus} : {kisa.autot[i].current_matka:.0f} km\n")
            print(f"Tämänhetkinen nopeus: {kisa.autot[i].current_nopeus}km/h\n")
autot = []

sahkoauto = Sahko("ABC-15", 180, 30, 52.5)
autot.append(sahkoauto)

moottoriauto = Polttomoottori("ACD-123", 165, 40, 32.3)
autot.append(moottoriauto)

ajo = Kilpailu(autot)

laskuri = 1

while laskuri != 4:
    print(f"******TUNTI {laskuri}!******")
    ajo.tunti_kuluu()
    laskuri = laskuri + 1

print("***LOPPU***")




