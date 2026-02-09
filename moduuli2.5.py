luoti=13.3
naula=32*luoti
leiviska=20*naula
eka=int(input("Anna leiviskat:"))
toka=int(input("Anna naulat:"))
kolmas=int(input("Anna luodit:"))
grammat=((eka*leiviska)+(toka*naula)+(kolmas*luoti))
kilot=grammat//1000
lgrammat=grammat%1000
print("Massa nykymittojen mukaan:",kilot,"kiloa ja",lgrammat,"grammaa")