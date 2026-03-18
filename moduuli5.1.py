import random
summa=0
montako=int(input("Montako arpakuutiota on?"))
for i in range(montako):
    kuutio = random.randint(1, 6)
    summa=summa+kuutio
    print(f"Arpakuution silmäluvun summa on", kuutio)