#Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi, joka saa parametrinaan nopeuden muutoksen (km/h).

# Jos nopeuden muutos on negatiivinen, auto hidastaa. Metodin on muutettava auto-olion nopeus-ominaisuuden arvoa.

# Auton nopeus ei saa kasvaa huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi.

# Jatka pääohjelmaa siten, että auton nopeutta nostetaan ensin +30 km/h, sitten +70 km/h ja lopuksi +50 km/h.

# Tulosta tämän jälkeen auton nopeus.

# Tee sitten hätäjarrutus määräämällä nopeuden muutos -200 km/h ja tulosta uusi nopeus. Kuljettua matkaa ei tarvitse vielä päivittää.

class auto:
    def __init__(auto, rekisteritunnus, max_nopeus):
        auto.rekisteritunnus = rekisteritunnus
        auto.max_nopeus = max_nopeus
        auto.current_nopeus = 0
        auto.current_matka = 0

    def kiihdyta(auto, delta_nopeus):
        if auto.current_nopeus + delta_nopeus < 0:
            print("Auton nopeus ei voi alentua nollaa pienemmäksi.")
        elif auto.current_nopeus + delta_nopeus > auto.max_nopeus:
            print("Auton nopeus ei voi olla sen huippunopeutta suurempi.")
        else:
            auto.current_nopeus = auto.current_nopeus + delta_nopeus


def delta_nopeus(delta_nopeus):
    print(f"\nYritetään kiihdyttää {delta_nopeus}km/h..")
    auto.kiihdyta(auto1, delta_nopeus)
    print(f"Tämänhetkinen nopeus: {auto1.current_nopeus}km/h\n")


auto1 = auto("ABC-123",142)
print(f"---------------\nRekisteritunnus: {auto1.rekisteritunnus}\nHuippunopeus: {auto1.max_nopeus}km/h\nTämänhetkinen nopeus: {auto1.current_nopeus}km/h\n---------------")


delta_nopeus(30)
delta_nopeus(70)
delta_nopeus(50)

print("---------------\nÄkkijarrutus!")
delta_nopeus(-200)
