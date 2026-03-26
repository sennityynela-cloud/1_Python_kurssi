def yhteenlasku():
    print("Lukujen summa on:", a + b)
    return a+b
def vahennyslasku():
    print("Lukujen erotus on:", a - b)
    return a-b
def kertolasku():
    print("Lukujen tulo on:", a * b)
    return a*b
def jakolasku():
    print("Lukujen osamäärä on:", a / b)
    return a/b


print("TERVETULOA KÄYTTÄMÄÄN LASKINTA!")

while True:
    print("\nValitse mitä toimintoa haluat käyttää:\n A: Yhteenlasku \n B: Vähennyslasku \n C: Kertolasku"
          "\n D: Jakolasku")

    valinta = input("Valintasi (A-D, Q lopettaa): ").upper()

    if valinta == "Q":
        print("Ohjelma lopetetaan.")
        break

    a = float(input("Anna eka luku: "))
    b = float(input("Anna toka luku: "))

    if valinta == "A":
        print(yhteenlasku())
    elif valinta == "B":
        print(vahennyslasku())
    elif valinta == "C":
        print(kertolasku())
    elif valinta == "D":
        print(jakolasku())
    else:
        print("Virheellinen valinta tai luku.")

