oppilaat = {
    "Aake": ["Aake", 8, "Matematiikka"],
    "Mikko": ["Mikko", 9, "Biologia"],
    "Riku": ["Riku", 7, "Historia"]
}
print(f"Aaken vuosiluokka: {oppilaat['Aake'][1]}")
print(f"Mikon lempiaine: {oppilaat['Mikko'][2]}")
oppilaat["Riku"][2] = "Fysiikka"
oppilaat["Sofia"] = ["Sofia", 6, "Kuvataide"]
del oppilaat["Aake"]
print(oppilaat)