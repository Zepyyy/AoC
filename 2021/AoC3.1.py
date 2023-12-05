liste = open("AoC3.txt", "r").readlines()
NB, gamma, epsilon = 0, "", ""

for j in range(len(liste[0]) - 1):
    for i in liste:
        NB += int(i[j])

    if NB >= len(liste) / 2:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"
    NB = 0

print(int(gamma, 2) * int(epsilon, 2))
