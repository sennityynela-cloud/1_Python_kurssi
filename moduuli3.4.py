luku=int(input("Mikä vuosiluku?"))

if luku % 4 == 0:
    if luku % 100 == 0:
        if luku % 400 == 0:
            print(f"Vuosi",luku,"on karkausvuosi.")
        else:
            print(f"Vuosi",luku,"ei ole karkausvuosi.")
    else:
        print(f"Vuosi",luku,"on karkausvuosi.")
else:
    print(f"Vuosi",luku,"ei ole karkausvuosi.")