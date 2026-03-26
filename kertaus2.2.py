arvot = []
arvot2 = []
while True:
    arvo = float(input("Syötä luku: "))
    arvot.append(arvo)
    arvot2.append(arvo)
    arvot2.sort()
    print("Arvot lisäysjärjestyksessä: ", arvot)
    print("Arvot suuruusjärjestyksessä: ",arvot2)
    if arvo == 0:
        print("Ohjelma päättyy.")
        break