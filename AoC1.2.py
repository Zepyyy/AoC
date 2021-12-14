liste = open("C:\\Users\\quent\\Desktop\\AoC2021\\AoC1.txt", "r").readlines()
sup = 0

for i,j in enumerate(liste):
    if int(i) < len(liste)-3:
        if int(liste[i+1]) + int(liste[i+2]) + int(liste[i+3]) > int(j) + int(liste[i+1]) + int(liste[i+2]):
            sup+=1
print(sup)
