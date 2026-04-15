asemat={ "LOWW" : "Wien",
         "EFHK" : "Helsinki",
         "EDDB" : "Berliini"}

while True:
    kysymys = int(input("Haluatko syöttää uuden lentoaseman (1), hakea jo syötetyn lentoaseman tiedot (2) vai lopettaa (3)?"))
    if kysymys == 3:
        print("Ohjelma päättyy.")
        break
    if kysymys == 1:
        koodi=str(input("Mikä on lentoaseman ICAO-koodi? ")).upper()
        nimi=str(input("Mikä on lentoaseman nimi?")).upper()
        asemat[koodi]=nimi
        print("Uuden lentoaseman tiedot ovat syötetty järjestelmään.")
    if kysymys == 2:
        hakukoodi=str(input("Mikä on lentoaseman ICAO-koodi? ")).upper()
        if hakukoodi in asemat:
            print("Koodi vastaa lentoasemaa:" ,asemat[hakukoodi])
        else:
            print("Asemaa ei ole järjestelmässä.")