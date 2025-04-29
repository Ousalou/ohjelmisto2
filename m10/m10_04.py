# Tehtävä on jatkoa aiemmalle autokilpailutehtävälle.
# Kirjoita Kilpailu-luokka,
# jolla on ominaisuuksina
# kilpailun nimi,
# pituus kilometreinä
# ja osallistuvien autojen lista.
#
# Luokassa on alustaja, joka saa parametreinaan nimen, kilometrimäärän ja autolistan ja asettaa ne ominaisuuksille arvoiksi. Luokassa on seuraavat metodit:

#tunti_kuluu, joka toteuttaa aiemmassa autokilpailutehtävässä mainitut tunnin välein tehtävät toimenpiteet eli arpoo kunkin auton nopeuden muutoksen ja kutsuu kullekin autolle kulje-metodia.

#tulosta_tilanne, joka tulostaa kaikkien autojen sen hetkiset tiedot selkeäksi taulukoksi muotoiltuna

#kilpailu_ohi, joka palauttaa True, jos jokin autoista on maalissa eli se on ajanut vähintään kilpailun kokonaiskilometrimäärän. Muussa tapauksessa palautetaan False


# Kirjoita pääohjelma, joka luo 8000 kilometrin kilpailun liniment "Suuri romuralli".
# Luotavalle kilpailulle annetaan kymmenen auton lista samaan tapaan kuin aiemmassa tehtävässä.
# Pääohjelma simuloi kilpailun etenemistä kutsumalla toistorakenteessa tunti_kuluu-metodia, jonka jälkeen aina tarkistetaan kilpailu_ohi-metodin avulla, onko kilpailu ohi.

# Ajantasainen tilanne tulostetaan tulosta tilanne-metodin avulla kymmenen tunnin välein sekä kertaalleen sen jälkeen, kun kilpailu on päättynyt.


import random
tunti_laskuri = 0

class Kilpailu:
    def __init__(kisa, nimi, pituus):
        kisa.autot = []
        for i in range(0,10):
            auto = Auto()
            kisa.autot.append(auto)
        kisa.nimi = nimi
        kisa.pituus = int(pituus)

    def tunti_kuluu(kisa):
        for i in range (0, len(kisa.autot)):
            print(f"\nAUTO {kisa.autot[i].rekisteritunnus}\n-------------")
            delta_nopeus_rand = random.randint(-10, 15)
            print(f"\nYritetään kiihdyttää autoa {kisa.autot[i].rekisteritunnus} {delta_nopeus_rand}km/h ....")
            kisa.autot[i].kiihdyta(delta_nopeus_rand)
            print(f"Tämänhetkinen kuljettu matka autolla {kisa.autot[i].rekisteritunnus} : {kisa.autot[i].current_matka:.0f} km\n")
            print(f"Tämänhetkinen nopeus: {kisa.autot[i].current_nopeus}km/h\n")

    def tulosta_tilanne(kisa):
        tilanne_lista = sorted(kisa.autot, key=lambda x: x.current_matka, reverse=True)
        print(f"{'-' * 80}")
        print(f"{'Rekisteritunnus':<20} | {'Nopeus nyt':<20} | {'Kuljettu matka':<21} |")
        print(f"{'-' * 80}")
        for i in tilanne_lista:
            print(f"{'-' * 80}")
            print(f"{i.rekisteritunnus:<20} | {i.current_nopeus:<20} | {i.current_matka:<21} |")
            print(f"{'-' * 80}")
        print(f"{'-' * 80}")

    def kilpailu_ohi(kisa):
        for i in range(len(kisa.autot)):
            if kisa.autot[i].current_matka >= 8000:
                return True
        return False

class Auto:
    def __init__(auto):
        auto.rekisteritunnus = f"{random.choice('ABCDEFGHIJKLMNOPQRSTUWVXYZ')}{random.choice('ABCDEFGHIJKLMNOPQRSTUWVXYZ')}{random.choice('ABCDEFGHIJKLMNOPQRSTUWVXYZ')}-{random.randint(1, 9)}{random.randint(1, 9)}{random.randint(1, 9)}"
        auto.max_nopeus = int(random.randint(100, 200))
        auto.current_nopeus = 0
        auto.current_matka = 0

    def add_matka(auto):
        auto.current_matka = auto.current_matka + auto.current_nopeus

    def kiihdyta(auto, delta_nopeus_rand):
        nopeus_check = auto.current_nopeus
        if nopeus_check + delta_nopeus_rand < 0:
            print("Auton nopeus ei voi alentua nollaa pienemmäksi.")
            auto.current_nopeus = 0
            print(f"Uusi nopeus on {auto.current_nopeus}km/h.")
        elif nopeus_check + delta_nopeus_rand > auto.max_nopeus:
            print("Auton nopeus ei voi olla sen huippunopeutta suurempi.")
        else:
            auto.current_nopeus = auto.current_nopeus + delta_nopeus_rand
        auto.current_matka = auto.current_matka + auto.current_nopeus

ralli = Kilpailu("Suuri romuralli", 8000)

kisa_ohi = False
h_counter = 10

while not kisa_ohi:
    Kilpailu.tunti_kuluu(ralli)
    kisa_ohi = Kilpailu.kilpailu_ohi(ralli)
    h_counter = h_counter - 1
    if h_counter == 1:
        Kilpailu.tulosta_tilanne(ralli)
        h_counter = 10

print(f"\nKilpailu ohi!\n")
Kilpailu.tulosta_tilanne(ralli)
