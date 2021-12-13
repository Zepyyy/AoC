liste = open("C:\\Users\\quent\\Desktop\\AoC2021\\AoC3.txt", "r").readlines()
NB, gamma, epsilon = 0, "", ""

for j in range(len(liste[0]) - 1):
    for i in liste:
        if i[j] == "1":
            NB += 1

    if NB >= len(liste) / 2:
        gamma += "1"
    else:
        gamma += "0"
    NB = 0
for i in gamma:
    if i == "1":
        epsilon += "0"
    else:
        epsilon += "1"

print(int(gamma, 2) * int(epsilon, 2))
