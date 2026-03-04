vsana = ""
tarina=""
while True:
    sana = str(input("Anna sana ('loppu' lopettaa):"))
    if sana == "loppu" or sana == vsana:
        break
    tarina += sana + " "
    vsana = sana
print("\nTarinasi on:")
print(tarina)