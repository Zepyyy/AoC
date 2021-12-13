liste = open("C:\\users\\quent\\Desktop\\AoC2021\\AoC4.txt", "r").readlines()

a = str(liste[0]).split(",")
b = str(liste[1:]).split(",")
n = 0

for i in a:
    if n < 4:
        print(i)
        if i in b[n]:
            print("y")
        n += 1
    else:
        print()
        n = 0
