import random

def noppa():
    luku = random.randint(1, 6)
    return

while True:
    print("Heitä noppaa.")
    luku = random.randint(1, 6)
    noppa()
    if luku == 6:
        print("Sait luvun",luku)
        print("Peli päättyy.")
        break
    else:
        print("Sait luvun",luku)
        print("Noppapeli jatkuu.")
    continue