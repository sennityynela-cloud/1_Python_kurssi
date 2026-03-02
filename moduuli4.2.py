import math
tuuma=int(input("Anna mitta tuumissa (negatiivinen lopettaa):"))
while tuuma > 0:
    print(tuuma*2.54,"cm")
    tuuma = int(input("Anna mitta tuumissa (negatiivinen lopettaa):"))
print("Ohjelma lopettaa toimintansa.")