# Nyt ohjelmoidaan autokilpailu.
# Uuden auton kuljettu matka alustetaan automaattisesti nollaksi.

# Tee pääohjelman alussa lista, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta.
# Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä. Rekisteritunnus luodaan seuraavasti "ABC-1", "ABC-2" jne.
# Sitten kilpailu alkaa. Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:

# Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä. Tämä tehdään kutsumalla kiihdytä-metodia.
# Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. Tämä tehdään kutsumalla kulje-metodia.
# Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä. Lopuksi tulostetaan kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna.

import random

class Auto:
    def __init__(auto, rekisteritunnus, max_nopeus_rand):
        auto.rekisteritunnus = rekisteritunnus
        auto.max_nopeus = max_nopeus_rand
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

autot = []

for i in range(3):
    rekisteritunnus = f"{random.choice('ABCDEFGHIJKLMNOPQRSTUWVXYZ')}{random.choice('ABCDEFGHIJKLMNOPQRSTUWVXYZ')}{random.choice('ABCDEFGHIJKLMNOPQRSTUWVXYZ')}-{random.randint(1, 9)}{random.randint(1, 9)}{random.randint(1, 9)}"
    print(rekisteritunnus)
    max_nopeus_rand = int(random.randint(100, 200))
    print(max_nopeus_rand)
    auto = Auto(rekisteritunnus, max_nopeus_rand)
    autot.append(auto)
    print(f"{auto.rekisteritunnus}: {auto.current_nopeus}")

print(autot)
hour = 1

while True:
    print (f"\n-----------\n\n-----------\nTunti {hour}!!\n-----------\n\n-----------\n")
    loop_break = False
    for auto in autot:
        print(f"\n----------\nAUTO {auto.rekisteritunnus}\n-----------\n")
        delta_nopeus_rand = random.randint(-10,15)
        print(f"\nYritetään kiihdyttää autoa {autot.index(auto)+1} {delta_nopeus_rand}km/h ....")
        auto.kiihdyta(delta_nopeus_rand)
        print(f"Tämänhetkinen kuljettu matka autolla {autot.index(auto)+1} : {auto.current_matka:.0f} km\n")
        print(f"Tämänhetkinen nopeus: {auto.current_nopeus}km/h\n")
        if auto.current_matka >= 100:
            print(f"\n----------\n\n----------\n\n----------\nAuto {auto.rekisteritunnus} on saavuttanut 10 000km!")
            voittaja = auto.rekisteritunnus
            loop_break = True
            break
    if loop_break == True:
        break
    hour = hour + 1

print("debug")

print(f"{'-'*80}")
print(f"{'Rekisteritunnus':<20} | {'Nopeus lopussa':<20} | {'Kuljettu matka':<18} | {'Ranking':<15}")
print(f"{'-'*80}")
for auto in autot:
    print(f"{auto.rekisteritunnus:<20} | {auto.current_nopeus:>2}{'km/h':<18} | {auto.current_matka:<5}{'km':<16}")
print(f"{'-'*80}")


