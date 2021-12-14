liste = [
    str(i)
    for i in open("C:\\users\\quent\\Desktop\\AoC2021\\AoC14.txt", "r").readlines()
]
elem = [str(i)[6] for i in liste[2:]]
paire = [str(i)[:2] for i in liste[2:]]
polymer = [str(i) for i in liste[0].replace("\n", "")]

jour = 10
templiste = ""

for j in range(jour):
    for i in range(len(polymer)):
        if i < len(polymer) - 1:
            index = paire.index(polymer[i] + polymer[i + 1])
            templiste += str(paire[index][0] + elem[index])
        elif i == len(polymer) - 1:
            index = paire.index(polymer[i - 1] + polymer[i])
            templiste += paire[index][1]
        else:
            index = paire.index(polymer[i - 1] + polymer[i])
            templiste += paire[index][0] + elem[index] + paire[index][1]
    polymer = templiste
    templiste = []
    print("jour: ", j + 1)
    print("taille: ", len(polymer))


print("end")
maxi = polymer.count(max(set(polymer), key=polymer.count))
mini = polymer.count(min(set(polymer), key=polymer.count))
print(max(set(polymer), key=polymer.count), maxi)
print(min(set(polymer), key=polymer.count), mini)


print("maxi - mini: ", maxi - mini)
