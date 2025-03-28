#Kirjoita Hissi-luokka, joka saa alustajaparametreinaan alimman ja ylimmän kerroksen numeron.
# Hissillä on metodit siirry_kerrokseen, kerros_ylös ja kerros_alas.
# Uusi hissi on aina alimmassa kerroksessa.
# Jos tee luodulle hissille h esimerkiksi metodikutsun h.siirry_kerrokseen(5),
# metodi kutsuu joko kerros_ylös- tai kerros_alas-metodia niin monta kertaa, että hissi päätyy viidenteen kerrokseen.
# Viimeksi mainitut metodit ajavat hissiä yhden kerroksen ylös- tai alaspäin ja ilmoittavat, missä kerroksessa hissi sen jälkeen on.
# Testaa luokkaa siten, että teet pääohjelmassa hissin ja käsket sen siirtymään haluamaasi kerrokseen ja sen jälkeen takaisin alimpaan kerrokseen.

class Hissi:
    def __init__(hissi, max_kerros, min_kerros):
        hissi.sijainti = min_kerros
        hissi.max_kerros = max_kerros
        hissi.min_kerros = min_kerros

    def siirry_kerrokseen(hissi, kerros):
        if hissi.sijainti == kerros:
            print(f"Hissi on jo kerroksessa {kerros}.")
        elif hissi.sijainti > kerros:
            print(f"Painetaan nappia {kerros}!")
            hissi.kerros_alas(kerros)
        elif hissi.sijainti < kerros:
            print(f"Painetaan nappia {kerros}!")
            hissi.kerros_ylos(kerros)
        else:
            pass

    def kerros_ylos(hissi, kerros):
        siirtyma = kerros - hissi.sijainti
        for i in range(siirtyma):
            hissi.sijainti = hissi.sijainti + 1
            print(f"Siirrytään kerrokseen {hissi.sijainti}...")
        print(f"Hissi on nyt kerroksessa {hissi.sijainti}.")


    def kerros_alas(hissi, kerros):
        siirtyma = hissi.sijainti - kerros
        for i in range(siirtyma):
            hissi.sijainti = hissi.sijainti - 1
            print(f"Siirrytään kerrokseen {hissi.sijainti}...")
        print(f"Hissi on nyt kerroksessa {hissi.sijainti}.")

h1 = Hissi(10, 1)
while True:
    kerros = int(input("Mihin kerrokseen haluat mennä? "))
    Hissi.siirry_kerrokseen(h1, kerros)
    if kerros == "":
        break

print("debug")
