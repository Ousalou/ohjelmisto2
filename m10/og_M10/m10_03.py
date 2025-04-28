#Jatka edellisen tehtävän ohjelmaa siten, että
# Talo-luokassa on parametriton metodi palohälytys, joka käskee kaikki hissit pohjakerrokseen.
# Jatka pääohjelmaa siten, että talossasi tulee palohälytys.

import random

class Hissi:
    def __init__(self, min_kerros, max_kerros, hissi_numero):
        self.min_kerros = min_kerros
        self.max_kerros = max_kerros
        self.sijainti = 1
        self.numero = hissi_numero

    def loyda_self(self, selfn_numero):
        pass

    def siirry_kerrokseen(self, kerros):
        if self.sijainti == kerros:
            print(f"self on jo kerroksessa {kerros}.")
        if kerros > self.max_kerros or kerros < self.min_kerros:
            print("Tuota kerrosta ei ole!")
        elif self.sijainti > kerros:
            print(f"Painetaan nappia {kerros}!")
            siirtyma = self.sijainti - kerros
            for i in range(siirtyma):
                self.kerros_alas()
        elif self.sijainti < kerros:
            print(f"Painetaan nappia {kerros}!")
            siirtyma = kerros - self.sijainti
            for i in range(siirtyma):
                self.kerros_ylos()
        return self.numero, self.sijainti

    def kerros_ylos(self):
        self.sijainti = self.sijainti + 1
        print(f"Siirrytään kerrokseen {self.sijainti}...")
        print(f"Hissi on nyt kerroksessa {self.sijainti}.")


    def kerros_alas(self):
        self.sijainti = self.sijainti - 1
        print(f"Siirrytään kerrokseen {self.sijainti}...")
        print(f"Hissi on nyt kerroksessa {self.sijainti}.")

    def hissin_kerros(self):
        return self.sijainti

class Talo:
    def __init__(self, min_kerros, max_kerros):
        self.min_kerros = 1
        self.max_kerros = max_kerros
        if self.max_kerros <= 3:
            self.hissit_amount = 1
        else:
            self.hissit_amount = max_kerros - (max_kerros // 2)
        self.hissit = self.luo_hissit(self.hissit_amount, min_kerros, max_kerros)

    def luo_hissit(self, hissit_amount, min_kerros, max_kerros):
        hissit = []
        global hissi_i
        for i in range(hissit_amount):
            hissi_i = f"hissi{i}"
            hissi_numero = i + 1
            hissi_i = Hissi(min_kerros, max_kerros, hissi_numero)
            hissit.append(hissi_i)
        print(hissit)
        return hissit

    def aja_hissia(self, hissi_numero):
        kerros = int(input("Mihin kerrokseen haluat mennä? "))
        self.hissit[hissi_numero-1].siirry_kerrokseen(kerros)

    def palohalytys(self):
        print(f"\nPalohälytys! Siirretään kaikki hissit takaisin kerrokseen 1.")
        for hissi_i in hissi.hissit:
            hissi_i.sijainti = 1


min_kerros = 1
max_kerros = int(input("Anna ylimmän kerroksen numero: "))
hissi = Talo(min_kerros, max_kerros)
print(f"Talossa on {hissi.hissit_amount} hissiä.")

palo_arpa = 0
while palo_arpa != 1:
    hissi_numero_int = int(input("Mitä hisseistä haluat ajaa? "))
    hissi.aja_hissia(hissi_numero_int)
    print(f"Hissi {hissi.numero} on nyt kerroksessa {hissi.hissit[hissi_numero_int - 1].hissin_kerros()}")
    palo_arpa = random.randint(1, 1)
hissi_numero = 3
hissi.aja_hissia(hissi_numero)

hissi.palohalytys()

for hissi_i in hissi.hissit:
    print(f"Hissi {hissi_i.numero} on nyt kerroksessa {hissi_i.sijainti}.")


