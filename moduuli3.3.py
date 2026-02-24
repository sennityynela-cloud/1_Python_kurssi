sukupuoli=str(input("Mikä on biologinen sukupuolesi?"))
arvo=int(input("Mikä on hemoglobiiniarvosi (g/l)?"))

if sukupuoli == "nainen":
    if arvo < 117:
        print("Hemoglobiiniarvosi on alhainen.")
    elif 117 <= arvo <= 175:
        print("Hemoglobiiiniarvosi on normaali.")
    elif arvo >= 175:
        print("Hemoglobiiniarvosi on korkea.")
if sukupuoli == "mies":
    if arvo < 134:
        print("Hemoglobiiniarvosi on alhainen.")
    elif 134 <= arvo <= 195:
        print("Hemoglobiiniarvosi on normaali.")
    elif arvo >= 195:
        print("Hemoglobiiniarvosi on korkea.")