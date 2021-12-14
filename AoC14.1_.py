liste = [
    str(i)
    for i in open("C:\\users\\quent\\Desktop\\AoC2021\\AoC14.txt", "r").readlines()
]
paire = [str(i)[6] for i in liste[2:]]
elem = [str(i)[:2] for i in liste[2:]]
polymer = [liste[0].replace("\n", "")]
jour = 5

print("polymer: ", polymer)
print("paire: ", paire)
print("elem: ", elem)


for i in range(jour):
    print("jour: ", i + 1)
