#Kirjoita Hissi-luokka, joka saa alustajaparametreinaan alimman ja ylimmän kerroksen numeron.
# Hissillä on metodit siirry_kerrokseen, kerros_ylös ja kerros_alas.
# Uusi hissi on aina alimmassa kerroksessa.
# Jos teet luodulle hissille h esimerkiksi metodikutsun h.siirry_kerrokseen(5),
# metodi kutsuu joko kerros_ylös- tai kerros_alas-metodia niin monta kertaa, että hissi päätyy viidenteen kerrokseen.
# Viimeksi mainitut metodit ajavat hissiä yhden kerroksen ylös- tai alaspäin ja ilmoittavat, missä kerroksessa hissi sen jälkeen on.
# Testaa luokkaa siten, että teet pääohjelmassa hissin ja käsket sen siirtymään haluamaasi kerrokseen ja sen jälkeen takaisin alimpaan kerrokseen.

class Elevator:
    hissit = 0

    def __init__(self, max_floor):
        self.max_floor = max_floor
        self.min_floor = 1
        self.current_floor = 1

    def kerros_alas(self, move_to_floor):
        while self.current_floor != move_to_floor:
            self.current_floor = self.current_floor - 1
            print(f".... olemme kerroksessa {self.current_floor} ....")
        print(f"\n Olemme saapuneet kerrokseen {self.current_floor}!\n")

    def kerros_ylos(self, move_to_floor):
        while self.current_floor != move_to_floor:
            self.current_floor = self.current_floor + 1
            print(f".... olemme kerroksessa {self.current_floor} ....")
        print(f"\n Olemme saapuneet kerrokseen {self.current_floor}!\n")

    def siirry_kerrokseen(self, move_to_floor):
        print(f"\nOlemme kerroksessa {self.current_floor}\nSiirrytään kerrokseen {move_to_floor}!\n")
        if move_to_floor > self.max_floor:
            print(f"Ylin kerros on {self.max_floor}!\n")
        elif move_to_floor < self.min_floor:
            print(f"Alin kerros on {self.min_floor}!\n")
        elif self.current_floor > move_to_floor:
            self.kerros_alas(move_to_floor)
        elif self.current_floor < move_to_floor:
            self.kerros_ylos(move_to_floor)
        elif self.current_floor == move_to_floor:
            print(f"Olet jo kerroksessa {self.current_floor}!\n")

h = Elevator(10)

h.siirry_kerrokseen(5)
h.siirry_kerrokseen(2)
h.siirry_kerrokseen(10)
h.siirry_kerrokseen(0)
h.siirry_kerrokseen(1)
