nimi=str(input("Mikä on nimesi?"))
if nimi != "Matti".lower():
    keittoannos=int(input("Mikä on keittoannosten määrä?"))
    print(f"Kokonaishinta on",keittoannos*5.9,"euroa")