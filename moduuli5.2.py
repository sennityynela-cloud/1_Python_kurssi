lista = []
while True:
    luku = input("Anna luku (tyhjä lopettaa):")
    if luku == " ":
        break
    luvut=int(luku)
    lista.append(luvut)
lista.sort(reverse=True)
print(f"Viisi suurinta lukua:",lista[:5])