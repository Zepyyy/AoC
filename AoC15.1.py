from itertools import combinations

liste = [
    str(i)
    for i in open("C:\\users\\quent\\Desktop\\AoC2021\\AoC15.txt", "r").readlines()
]

li = []
Curseur = [0, 0]
Compteur = 0
path = []
risk = 0
z = []
e = ""

for i in liste:
    i = i.replace("\n", "")
    li.append(i)

print(len(li) - 1)

"""for i in range(len(li)):
    for j in range(len(li)):
        e += str(i) + "," + str(j)
        e = e.split(",")
        e = [int(i) for i in e]
        z.append(e)
        e = """ ""

while Curseur != [len(li) - 1, len(li) - 1]:

    if Curseur[0] + 1 != len(li) and Curseur[1] + 1 != len(li):
        print(
            li[(Curseur[0] + 1)][Curseur[1]], "<", li[Curseur[0]][(Curseur[1]) + 1], "?"
        )

        if (
            li[(Curseur[0] + 1)][Curseur[1]] < li[Curseur[0]][(Curseur[1] + 1)]
            or Curseur[1] == len(li) - 1
        ):
            print("okay")
            Curseur = [Curseur[0] + 1, Curseur[1]]
            risk += int(li[Curseur[0]][Curseur[1]])
            print(Curseur)
            path.append(Curseur)
            print("li: ", li[Curseur[0]][Curseur[1]] + "\n")
        elif (
            li[(Curseur[0] + 1)][Curseur[1]] >= li[Curseur[0]][(Curseur[1] + 1)]
            or Curseur[0] == len(li) - 1
        ):
            print("Nope")
            Curseur = [Curseur[0], Curseur[1] + 1]
            risk += int(li[Curseur[0]][Curseur[1]])
            print(Curseur)
            path.append(Curseur)
            print("li: ", li[Curseur[0]][Curseur[1]] + "\n")
    else:
        Curseur = [len(li) - 1, len(li) - 1]
        risk += int(li[Curseur[0]][Curseur[1]])
        print(Curseur)
        path.append(Curseur)
        print("li: ", li[Curseur[0]][Curseur[1]] + "\n")


print("endedn")
print("path: ", path)
print("risk: ", risk)
"""print(z)"""

# li[1][2] -> X = 2, Y = 1
# Curseur = [1, 2] -> X = 2, Y = 1

# print(li[Curseur[0]][Curseur[1]]) = 8
# print(li[1][2]) = 8
