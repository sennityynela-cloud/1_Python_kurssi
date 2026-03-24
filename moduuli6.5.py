def parittomatpois(lista):
    u_lista= []
    for luku in lista:
        if luku % 2 == 0:
            u_lista.append(luku)
    return u_lista

alkuperainen= [1, 2, 3, 4]
karsittu= parittomatpois(alkuperainen)

print("Alkuperäinen lista:",alkuperainen)
print("Pelkät parilliset:",karsittu)