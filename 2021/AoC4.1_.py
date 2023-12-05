liste = open("C:\\users\\quent\\Desktop\\AoC2021\\AoC4.txt", "r").readlines()
liste1 = []
a = str(liste[0]).split(",")
b = str(liste[1:]).split(",")
n = 0

for i in range(len(b) - 1):
    if i % 5 == 0:
        liste1.append(b[i])

print(liste1)
