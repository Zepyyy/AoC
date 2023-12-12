def start():
    with open("9.txt", "r") as f:
        input = f.read().splitlines()
        return input

def extrapolate(line,last=[]):
    if last == []:
        last.append(line[0])
    nr = []
    for i in range(len(line)-1, 0, -1):
        nr.append(int(line[i])-int(line[i-1]))
    last.append(nr[-1])
    nr.reverse()
    
    # print(f"line: {line}, nr: {nr}")
    extrapolate(nr, last) if not [x for x in nr if len(nr)==nr.count(0)] else print("aled")
    # print(f"last: {last}")
    return last

def ex(input):
    euh = []
    total = 0
    extra = []
    for line in input:
        nrs = [int(x) for x in line.split()]
        euh.append(extrapolate(nrs,[]))
    # print(euh)
    for i in range(len(euh)):
        aled = euh[i]
        # print(f"aled: {aled}")
        for y in range(len(aled)-1,-1,-1):
            if extra == []:
                extra.append(0)
            else:
                extra.append(aled[y]-extra[-1])
            # print(f"extra: {extra}")
        total += extra[-1]
        extra = []
    return total

print(ex(start()))