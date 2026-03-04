import math
while True:
    laskutoimitus = str(input("Anna laskutoimitus ('Lopeta' päättää ohjelman):")).lower()
    if laskutoimitus == "lopeta":
        print("Ohjelma päättyy.")
        break
    luku1 = float(input("Anna luku: "))
    luku2 = float(input("Anna toinen luku:"))
    if laskutoimitus == "yhteenlasku":
        print("Tuloksesi:",luku1+luku2)
    elif laskutoimitus == "vähennyslasku":
        print("Tuloksesi:",luku1-luku2)
    elif laskutoimitus == "kertolasku":
        print("Tuloksesi:",luku1*luku2)
    elif laskutoimitus == "jakolasku":
        if luku2 != 0:
            print("Tuloksesi:",luku1/luku2)
        else:
            print("Ei voi jakaa nollalla.")
    else:
        print("En ymmärrä.")