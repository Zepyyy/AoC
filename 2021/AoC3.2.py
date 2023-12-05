liste = open("AoC3.txt", "r").read().splitlines()
count = 0
templist = []
bit02 = ""
bitCO2 = ""

for j in range(len(liste[0])):
    if len(liste) == 1:
        bit02 = liste[0]
    else:
        for i in liste:
            count += int(i[j])
        if count >= len(liste) / 2:
            bit02 += "1"
            count = 0
        else:
            bit02 += "0"
            count = 0
        for k in range(len(liste)):
            if liste[k][j] == bit02[j]:
                templist.append(liste[k])
        liste = templist
        templist = []

liste = open("AoC3.txt", "r").read().splitlines()
templist = []
count = 0
bitCO2 = ""

for j in range(len(liste[0])):
    if len(liste) == 1:
        bitCO2 = liste[0]
    else:
        for i in liste:
            count += int(i[j])
        if count < len(liste) / 2:
            bitCO2 += "1"
            count = 0
        else:
            bitCO2 += "0"
            count = 0
        for k in range(len(liste)):
            if liste[k][j] == bitCO2[j]:
                templist.append(liste[k])
        liste = templist
        templist = []
print(int(bit02, 2) * int(bitCO2, 2))
