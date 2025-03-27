#Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan tuntimäärän.
# Metodi kasvattaa kuljettua matkaa sen verran kuin auto on tasaisella vauhdilla annetussa tuntimäärässä edennyt.
# Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km. Nopeus on 60 km/h. Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan lukemaan 2090 km.

class auto:
    def __init__(auto, rekisteritunnus, max_nopeus):
        auto.rekisteritunnus = rekisteritunnus
        auto.max_nopeus = max_nopeus
        auto.current_nopeus = 0
        auto.current_matka = 2000

    def add_matka(auto, delta_time):
        auto.current_matka = auto.current_matka + (delta_time * auto.current_nopeus)

    def kiihdyta(auto, delta_nopeus, delta_time):
        if auto.current_nopeus + delta_nopeus < 0:
            print("Auton nopeus ei voi alentua nollaa pienemmäksi.")
        elif auto.current_nopeus + delta_nopeus > auto.max_nopeus:
            print("Auton nopeus ei voi olla sen huippunopeutta suurempi.")
        else:
            auto.current_nopeus = auto.current_nopeus + delta_nopeus


def delta_nopeus(delta_nopeus, delta_time):
    print(f"\nYritetään kiihdyttää {delta_nopeus}km/h ....")
    auto.kiihdyta(auto1, delta_nopeus, delta_time)
    print(f"Tämänhetkinen nopeus: {auto1.current_nopeus}km/h\n")
    auto.add_matka(auto1, delta_time)
    print(f"Tämänhetkinen kuljettu matka: {auto1.current_matka:.0f} km\n")


auto1 = auto("ABC-123",142)
print(f"---------------\nRekisteritunnus: {auto1.rekisteritunnus}\nHuippunopeus: {auto1.max_nopeus}km/h\nTämänhetkinen nopeus: {auto1.current_nopeus}km/h\nKuljettu matka:{auto1.current_matka} km\n---------------")


delta_nopeus(60, 1.5)
