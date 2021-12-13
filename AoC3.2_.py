liste = open("C:\\Users\\quent\\Desktop\\AoC2021\\AoC3.txt", "r").read().splitlines()
print(liste)
NB, CO2, Oxygen, BIT = 0, "", "", ""
TempListe = []

for j in range(len(liste[0]) - 1):
    for i in liste:
        if BIT == "":
            TempListe.append(i)
            if i[j] == "1":
                NB += 1
            else:
                NB += 0
        else:
            TempListe = []
            if i[j - 1] == BIT[j - 1]:
                TempListe.append(i)
                if i[j] == "1":
                    NB += 1
                else:
                    NB += 0

    print("NB: ", NB)
    print("TempListe: ", TempListe)

    if NB >= len(TempListe) / 2:
        BIT += "1"
    else:
        BIT += "0"
    print("BIT: ", BIT)
    NB = 0


print("BIT: ", BIT)

"""
    print("NB: ", NB)
    if NB >= len(liste)/2:
        CO2 += '1'
    else:
        CO2 += '0'
    NB = 0


print("CO2: ", CO2)
print("epsilon: ", Oxygen)
print(int(CO2, 2))
print(int(Oxygen, 2))
print(int(CO2, 2)*int(Oxygen, 2))
"""
