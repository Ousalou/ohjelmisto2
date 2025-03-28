#Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan.
# Talon alustajaparametreina annetaan alimman ja ylimmän kerroksen numero sekä hissien lukumäärä.
# Talon luonnin yhteydessä talo luo tarvittavan määrän hissejä. Hissien lista tallennetaan talon ominaisuutena.
# Kirjoita taloon metodi aja_hissiä, joka saa parametreinaan hissin numeron ja kohdekerroksen. Kirjoita pääohjelmaan lauseet talon luomiseksi ja talon hisseillä ajelemiseksi.

class Hissi:
    def __init__(hissi, min_kerros, max_kerros, hissi_numero):
        hissi.min_kerros = min_kerros
        hissi.max_kerros = max_kerros
        sijainti = min_kerros
        hissi.sijainti = 1
        hissi.numero = hissi_numero

    def loyda_hissi(hissi, hissin_numero):
        pass

    def siirry_kerrokseen(hissi, kerros):
        if hissi.sijainti == kerros:
            print(f"Hissi on jo kerroksessa {kerros}.")
        if kerros > hissi.max_kerros and kerros > hissi.min_kerros:
            print("Tuota kerrosta ei ole!")
        elif hissi.sijainti > kerros:
            print(f"Painetaan nappia {kerros}!")
            siirtyma = hissi.sijainti - kerros
            for i in range(siirtyma):
                hissi.kerros_alas()
        elif hissi.sijainti < kerros:
            print(f"Painetaan nappia {kerros}!")
            siirtyma = kerros - hissi.sijainti
            for i in range(siirtyma):
                hissi.kerros_ylos()
        return hissi.numero, hissi.sijainti

    def kerros_ylos(hissi):
        hissi.sijainti = hissi.sijainti + 1
        print(f"Siirrytään kerrokseen {hissi.sijainti}...")
        print(f"Hissi on nyt kerroksessa {hissi.sijainti}.")


    def kerros_alas(hissi):
        hissi.sijainti = hissi.sijainti - 1
        print(f"Siirrytään kerrokseen {hissi.sijainti}...")
        print(f"Hissi on nyt kerroksessa {hissi.sijainti}.")

    def hissin_kerros(hissi, hissi_numero):
        pass

class Talo:
    def __init__(talo, min_kerros, max_kerros):
        talo.min_kerros = min_kerros
        talo.max_kerros = max_kerros
        if talo.max_kerros <= 3:
            talo.hissit_amount = 1
        else:
            talo.hissit_amount = max_kerros - (max_kerros // 2)
        hissit_amount = talo.hissit_amount
        talo.hissit = talo.luo_hissit(hissit_amount, min_kerros, max_kerros)


    def luo_hissit(talo, hissit_amount, min_kerros, max_kerros):
        hissit = []
        global hissi_i
        for i in range(hissit_amount):
            hissi_i = f"hissi{i}"
            hissi_numero = i + 1
            hissi_i = Hissi(min_kerros, max_kerros, hissi_numero)
            hissit.append(hissi_i)
        print(hissit)
        return hissit

    def aja_hissia(talo, hissi, kerros):
        Hissi.siirry_kerrokseen(hissi, kerros)

while True:
    min_kerros = int(input("Anna ensimmäisen kerroksen numero: "))
    max_kerros = int(input("Anna ylimmän kerroksen numero: "))
    talo = Talo(min_kerros, max_kerros)
    print(f"Talossa on {talo.hissit_amount} hissiä.")
    hissi_numero = int(input("Mitä hisseistä haluat ajaa? "))
    kerros = int(input("Mihin kerrokseen haluat mennä? "))
    hissi = f"hissi{hissi_numero}"
    talo.aja_hissia(hissi, kerros)
    print (f"Hissi {hissi_numero} on nyt kerroksessa {Hissi.hissin_kerros(hissi)}")




