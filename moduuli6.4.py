def l_summa(luvut):
    summa= 0
    for luku in luvut:
        summa += luku
    return summa
lista= [3,3,5,2,1,6]
tulos= l_summa(lista)
print("Listan lukujen summa on",tulos)