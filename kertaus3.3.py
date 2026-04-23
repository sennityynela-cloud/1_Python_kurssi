kirjasto = {
    "Sinkkuelämää": ["Candace Bushnell", 1996, "Chick lit"],
    "Muumimaailma": ["Tove Jansson", 1945, "Lastenkirjallisuus"],
    "Mitä Missä Milloin": ["Toimituskunta", 1950, "Tietokirja"]
}
print(f"Kirjoittaja: {kirjasto['Sinkkuelämää'][0]}")
print(f"Genre: {kirjasto['Mitä Missä Milloin'][2]}")
kirjasto["Muumimaailma"][2] = "Fantasia"
kirjasto["Sinuhe egyptiläinen"] = ["Mika Waltari", 1945, "Klassikko"]
del kirjasto["Sinkkuelämää"]
print(kirjasto)