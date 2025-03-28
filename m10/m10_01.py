#Kirjoita Hissi-luokka, joka saa alustajaparametreinaan alimman ja ylimmän kerroksen numeron.
# Hissillä on metodit siirry_kerrokseen, kerros_ylös ja kerros_alas.
# Uusi hissi on aina alimmassa kerroksessa.
# Jos tee luodulle hissille h esimerkiksi metodikutsun h.siirry_kerrokseen(5),
# metodi kutsuu joko kerros_ylös- tai kerros_alas-metodia niin monta kertaa, että hissi päätyy viidenteen kerrokseen.
# Viimeksi mainitut metodit ajavat hissiä yhden kerroksen ylös- tai alaspäin ja ilmoittavat, missä kerroksessa hissi sen jälkeen on.
# Testaa luokkaa siten, että teet pääohjelmassa hissin ja käsket sen siirtymään haluamaasi kerrokseen ja sen jälkeen takaisin alimpaan kerrokseen.

class Hissi:
    def __init__(hissi, max_kerros, min_kerros):
        alku_kerros = min_kerros
        hissi.sijainti = alku_kerros
        hissi.max_kerros = max_kerros
        hissi.min_kerros = min_kerros

    def hissin_kerros(hissi):
        return hissi.sijainti

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
        else:
            pass

    def kerros_ylos(hissi):
        hissi.sijainti = hissi.sijainti + 1
        print(f"Siirrytään kerrokseen {hissi.sijainti}...")
        print(f"Hissi on nyt kerroksessa {hissi.sijainti}.")


    def kerros_alas(hissi):
        hissi.sijainti = hissi.sijainti - 1
        print(f"Siirrytään kerrokseen {hissi.sijainti}...")
        print(f"Hissi on nyt kerroksessa {hissi.sijainti}.")

h1 = Hissi(10, 1)
while True:
    kerros = input("Mihin kerrokseen haluat mennä? ")
    if kerros == "":
        break
    kerros = int(kerros)
    Hissi.siirry_kerrokseen(h1, kerros)

kerros = Hissi.hissin_kerros(h1)
print(f"Ohjelma päättyi, olemme kerroksessa {kerros}.")
