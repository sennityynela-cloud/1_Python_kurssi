kayttajatunnus="python"
salasana="rules"
yritykset= 0
max_yritykset= 5
while yritykset < max_yritykset:
    kayttaja= input("Anna käyttäjätunnus: ")
    key= input("Anna salasana: ")
    if kayttaja==kayttajatunnus and key==salasana:
        print("Tervetuloa!")
        break
    else:
        yritykset += 1
        print(f"Väärin. Yrityksiä käytetty: {yritykset}/{max_yritykset}")
if yritykset == max_yritykset:
    print("Pääsy evätty.")
