# Kirjoita Auto-luokka,
# jonka ominaisuuksina ovat rekisteritunnus, huippunopeus, tämänhetkinen nopeus ja kuljettu matka.
# Kirjoita luokkaan alustaja, joka asettaa ominaisuuksista kaksi ensin mainittua parametreina saatuihin arvoihin.
# Uuden auton nopeus ja kuljetut matka on asetettava automaattisesti nollaksi.
# Kirjoita pääohjelma, jossa luot uuden auton (rekisteritunnus ABC-123, huippunopeus 142 km/h).
# Tulosta pääohjelmassa sen jälkeen luodun auton kaikki ominaisuudet.

class auto:
    def __init__(auto, rekisteritunnus, max_nopeus):
        auto.rekisteritunnus = rekisteritunnus
        auto.huippunopeus = max_nopeus
        auto.current_nopeus = 0
        auto.current_matka = 0

auto1 = auto("ABC-123",142)
print(f"Rekisteritunnus: {auto1.rekisteritunnus}\nHuippunopeus: {auto1.huippunopeus}km/h\nTämänhetkinen nopeus: {auto1.current_nopeus}km/h\nKuljettu matka:{auto1.current_matka}km")








