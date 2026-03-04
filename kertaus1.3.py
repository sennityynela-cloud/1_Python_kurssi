import math
from math import sqrt

kokonaisluku=int(input("Anna kokonaisluku (nolla lopettaa ohjelman):"))
while True:
    if kokonaisluku < 0:
        print("Virheellinen numero")
        kokonaisluku = int(input("Anna kokonaisluku (nolla lopettaa ohjelman):"))
        break
    elif kokonaisluku > 0:
        print(sqrt(kokonaisluku))
        kokonaisluku = int(input("Anna kokonaisluku (nolla lopettaa ohjelman):"))
    elif kokonaisluku == 0:
        print("Kiitos. Ohjelma päättyy.")
        break
