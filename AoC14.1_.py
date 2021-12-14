liste = [
    str(i)
    for i in open("C:\\users\\quent\\Desktop\\AoC2021\\AoC14.txt", "r").readlines()
]

polymer = liste[0]
table = liste[2:]

jour = 5

print(polymer)
print(table)

for i in range(jour):
    for j, l in enumerate(polymer):
        for k in table:
            print(k[:2])
            print(k[6])
    print("jour: ", i + 1)
