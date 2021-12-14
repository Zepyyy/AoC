liste = [
    int(i)
    for i in open("C:\\Users\\quent\\Desktop\\AoC2021\\AoC6.txt", "r")
    .readlines()[0]
    .split(",")
]
jours = 80

quantite = [0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in liste:
    if i == 0:
        quantite[0] += 1
    elif i == 1:
        quantite[1] += 1
    elif i == 2:
        quantite[2] += 1
    elif i == 3:
        quantite[3] += 1
    elif i == 4:
        quantite[4] += 1
    elif i == 5:
        quantite[5] += 1
    elif i == 6:
        quantite[6] += 1
    elif i == 7:
        quantite[7] += 1
    else:
        quantite[8] += 1
print(quantite)

for i in range(jours):
    zero = quantite[0]
    quantite[0] = quantite[1]
    quantite[1] = quantite[2]
    quantite[2] = quantite[3]
    quantite[3] = quantite[4]
    quantite[4] = quantite[5]
    quantite[5] = quantite[6]
    quantite[6] = quantite[7] + zero
    quantite[7] = quantite[8]
    quantite[8] = zero
print(sum(quantite))

