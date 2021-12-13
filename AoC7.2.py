liste = [
    int(i)
    for i in open("C:\\users\\quent\\Desktop\\AoC2021\\AoC7.txt", "r")
    .readlines()[0]
    .split(",")
]
m = []
mm = []

for j in range(max(liste) + 1):
    for i in liste:
        p = (abs(i - j) * (abs(i - j) + 1)) / 2
        m.append(p)
    a = sum(m)
    mm.append(a)
    m = []
print(min(mm))
