# Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron,
# jonka jälkeen ohjelma tulostaa sitä vastaavan vuodenajan (kevät, kesä, syksy, talvi).
# Tallenna ohjelmassasi kuukausia vastaavat vuodenajat merkkijonoina monikkotietorakenteeseen.
# Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten, että joulukuu on ensimmäinen talvikuukausi.

talvi=((12,"joulukuu"),(1,"tammikuu"),(2,"helmikuu"))
kevat=((3,"maaliskuu"), (4,"huhtikuu"),(5,"toukokuu"))
kesa=((6,"kesäkuu"),(7,"heinäkuu"),(8,"elokuu"))
syksy=((9,"syyskuu"),(10,"lokakuu"),(11,"marraskuu"))

numero=int(input("Anna kuukauden numero (1-12): "))

if numero == 12 or numero == 1 or numero == 2:
    print("Antamasi kuukausi on talvikuukausi.")
if numero == 3 or numero == 4 or numero == 5 :
    print("Antamasi kuukausi on kevätkuukausi.")
if numero == 6 or numero == 7 or numero == 8:
    print("Antamasi kuukausi on kesäkuukausi.")
if numero == 9 or numero == 10 or numero == 11:
    print("Antamasi kuukausi on syksykuukausi.")



