nimilista=set()

while True:
    nimi=str(input("Anna nimi. Ohjelma jatkuu siihen saakka kunnes syötät tyhjän merkkijonon. "))
    if nimi == "":
        print("Ohjelma päättyy.")
        break
    if nimi in nimilista:
        print("Aiemmin syötetty nimi.")
    elif nimi not in nimilista:
        nimilista.add(nimi)
        print("Uusi nimi.")
print(nimilista)