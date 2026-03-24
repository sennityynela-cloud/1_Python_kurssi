import math
def laske_yhinta(halkaisija,hinta):
    sade_m= (halkaisija / 2) / 100
    pinta_ala= math.pi*sade_m**2
    yhinta= hinta / pinta_ala
    return yhinta

halkaisija1= float(input("Anna ekan pizzan halkaisija (cm): "))
hinta1= float(input("Anna ekan pizzan hinta euroina: "))
halkaisija2= float(input("Anna tokan pizzan halkaisija (cm): "))
hinta2= float(input("Anna tokan pizzan hinta euroina: "))
yhinta1= laske_yhinta(halkaisija1, hinta1)
yhinta2= laske_yhinta(halkaisija2, hinta2)

if yhinta1 < yhinta2:
    print(f"Eka pizza antaa paremman vastineen rahalle ({yhinta1:.2f} e/m2).")
elif yhinta2 < yhinta1:
    print(f"Toka pizza antaa paremman vastineen rahalle ({yhinta2:.2f} e/m2).")
else:
    print("Molemmat pizzat ovat saman hintaisia per neliömetri.")