lista=["moi", "kynätkin","vesipullo","läppäri","kissa","tuoli","ihminen"]
kirjaimet= 0
len(lista)
for sana in lista:
    if len(sana)>=6:
        kirjaimet +=1
print("Listassa on",kirjaimet,"sanaa, jossa on enemmän kuin 5 kirjainta.")
