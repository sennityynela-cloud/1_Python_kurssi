def kuusi(koko):
    print("Tämä on kuusi!")

koko=int(input("Minkä kokoinen kuusi on?"))
for i in range(1, koko + 1):
    tahdet= "*" * (2 * i - 1)
    valit= " " * (koko - i)
    print(valit + tahdet)
    jalka= " " * (koko - 1)
    print(jalka + "*")

kuusi(koko)