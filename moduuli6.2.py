import random

def noppa(tahkot):
    luku = random.randint(1,tahkot)
    return luku

t_maara=int(input("Kuinka monta tahkoa nopassa on?"))

while True:
    print("Heitä noppaa.")
    luku = noppa(t_maara)
    if luku == t_maara:
        print("Sait maksimisilmäluvun",luku)
        print("Peli päättyy.")
        break
    else:
        print("Sait luvun",luku)
        print("Noppapeli jatkuu.")
    continue