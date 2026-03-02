pienin=None
suurin=None
while True:
    luku = input("Anna luku (tyhjä lopettaa):")
    if luku=="":
        break
    numero=int(luku)
    if pienin is None or numero<pienin:
        pienin=numero
    if suurin is None or numero>suurin:
        suurin=numero
    if pienin is not None:
        print("Pienin:",pienin)
        print("Suurin:",suurin)
print("Et syöttänyt lukua.")