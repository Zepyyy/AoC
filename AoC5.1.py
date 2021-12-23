liste = open("AoC5.txt", "r").read().splitlines()
temp = []
no = []
splitted = []
count = 0

for i in liste:
    i = i.replace(" -> ", ",")
    splitted = i.split(",", 3)
    x1 = int(splitted[0])
    x2 = int(splitted[2])
    y1 = int(splitted[1])
    y2 = int(splitted[3])
    if x1 == x2 or y1 == y2:
        point = [x1, y1], [x2, y2]
        temp.append(point)
print(temp)

for i in range(0, len(temp)):
    for j in range(0, len(temp)):
        if temp[i] != temp[j] and not (temp[j] in no):
            no.append(temp[i])
            x1 = temp[i][0][0]
            y1 = temp[i][0][1]
            x2 = temp[i][1][0]
            y2 = temp[i][1][1]
            x3 = temp[j][0][0]
            y3 = temp[j][0][1]
            x4 = temp[j][1][0]
            y4 = temp[j][1][1]
            maxx = max(x1, x2)
            maxy = max(y1, y2)
            minx = min(x1, x2)
            miny = min(y1, y2)
            if x1 == x2 or y1 == y2:
                if ((miny <= y3 <= maxy) or (miny <= y4 <= maxy)) and (
                    (minx <= x3 <= maxx) or (minx <= x4 <= maxx)
                ):
                    print(x1, y1, x2, y2)
                    print(x3, y3, x4, y4)
                    print("ya")
                    print("count:", count)
                    count += 1
                    if ((miny <= y3 <= maxy) and (miny <= y4 <= maxy)) and (
                        (minx <= x3 <= maxx) and (minx <= x4 <= maxx)
                    ):
                        c = abs((x1 - x3) + (y1 - y3) + (x2 - x4) + (y2 - y4))
                        count += c
                        print("count:", count)
                        count -= 1
print("count:", count)
print("finished")
