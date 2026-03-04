import math
tuntipalkka=float(input("Mikä on tuntipalkkasi?"))
tunnit=float(input("Montako tuntia olet tehnyt?"))
paiva=str(input("Mikä viikonpäivä on?"))
paivapalkka=tuntipalkka*tunnit
spaiva=paivapalkka*2

if paiva == "sunnuntai":
    print(f"Päiväpalkkasi on",spaiva,"euroa.")
else:
    print(f"Päiväpalkkasi on",paivapalkka,"euroa.")