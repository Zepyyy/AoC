from itertools import combinations

liste = open("AoC15.txt", "r").read().splitlines()

Curseur = [0, 0]
Compteur = 0
path = []
risk = 0
z = []
e = ""
print(len(liste) - 1)

"""for i in range(len(liste)):
    for j in range(len(liste)):
        e += str(i) + "," + str(j)
        e = e.split(",")
        e = [int(i) for i in e]
        z.append(e)
        e = """ ""

while Curseur != [len(liste) - 1, len(liste) - 1]:

    if Curseur[0] + 1 != len(liste) and Curseur[1] + 1 != len(liste):
        print(
            liste[(Curseur[0] + 1)][Curseur[1]],
            "<",
            liste[Curseur[0]][(Curseur[1]) + 1],
            "?",
        )

        if (
            liste[(Curseur[0] + 1)][Curseur[1]] < liste[Curseur[0]][(Curseur[1] + 1)]
            or Curseur[1] == len(liste) - 1
        ):
            print("okay")
            Curseur = [Curseur[0] + 1, Curseur[1]]
            risk += int(liste[Curseur[0]][Curseur[1]])
            print(Curseur)
            path.append(Curseur)
            print("liste: ", liste[Curseur[0]][Curseur[1]] + "\n")
        elif (
            liste[(Curseur[0] + 1)][Curseur[1]] >= liste[Curseur[0]][(Curseur[1] + 1)]
            or Curseur[0] == len(liste) - 1
        ):
            print("Nope")
            Curseur = [Curseur[0], Curseur[1] + 1]
            risk += int(liste[Curseur[0]][Curseur[1]])
            print(Curseur)
            path.append(Curseur)
            print("liste: ", liste[Curseur[0]][Curseur[1]] + "\n")
    else:
        Curseur = [len(liste) - 1, len(liste) - 1]
        risk += int(liste[Curseur[0]][Curseur[1]])
        print(Curseur)
        path.append(Curseur)
        print("liste: ", liste[Curseur[0]][Curseur[1]] + "\n")


print("endedn")
print("path: ", path)
print("risk: ", risk)
"""print(z)"""

# liste[1][2] -> X = 2, Y = 1
# Curseur = [1, 2] -> X = 2, Y = 1

# print(liste[Curseur[0]][Curseur[1]]) = 8
# print(liste[1][2]) = 8
