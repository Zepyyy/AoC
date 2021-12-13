liste = open("C:\\Users\\quent\\Desktop\\AoC2021\\AoC1.txt", "r").readlines()
sup = 0
for i,j in enumerate(liste):
    if int(j) - int(liste[i-1]) > 0:
        sup+=1
print(sup)