liste = [str(i) for i in open("AoC2.txt", "r").readlines()]
horizontal = 0
depths = 0

for i in liste:
    if i[0:2] == "up":
        depths -= int(i[3])
    elif i[0:4] == "down":
        depths += int(i[5])
    elif i[0:7] == "forward":
        horizontal += int(i[8])

print(horizontal * depths)
