def start():
    with open("9.txt", "r") as f:
        input = f.read().splitlines()
        return input

def extrapolate(line,last=[]):
    if last == []:
        last.append(line[-1])
    nr = []
    for i in range(0, len(line)-1):
        nr.append(int(line[i+1])-int(line[i]))
    last.append(nr[-1])
    
    # print(f"line: {line}, nr: {nr}")
    extrapolate(nr, last) if not [x for x in nr if len(nr)==nr.count(0)] else print("aled")
    # print(f"last: {last}")
    return last

def ex(input):
    euh = []
    total = 0
    for line in input:
        nrs = [int(x) for x in line.split()]
        euh.append(extrapolate(nrs,[]))
    # print(euh)
    for i in range(len(euh)):
        # print(f"i: {i}, euh[i]: {euh[i]}, euh[i][0]: {euh[i][0]}, sum(euh[i][1:]): {sum(euh[i][1:])}")
        total += (int(euh[i][0]) + sum(euh[i][1:]))
    return total

print(ex(start()))