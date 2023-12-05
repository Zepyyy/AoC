liste = [
    str(i)
    for i in open("C:\\Users\\quent\\Desktop\\AoC2021\\AoC10.txt", "r")
    .read()
    .split(",")
]

char = []
n = 0

for i in liste:
    if i[n] == "(":
        char.append("(")
    elif i[n] == "[":
        char.append("[")
    elif i[n] == "{":
        char.append("{")
    elif i[n] == "<":
        char.append("<")

    elif i[n] == ")":
        print("ok")
        n -= 1
    elif i[n] == "]":
        if char[:n] == "[":
            print("ok")
            n -= 1
    elif i[n] == "}":
        if char[:n] == "}":
            print("ok")
            n -= 1
    elif i[n] == ">":
        if char[:n] == "<":
            print("ok")
            n -= 1
    else:
        print("prob")
    n += 1

# for i, j in enumerate(liste):
"""if liste[i] == "(":
        char[0] += 1
    elif liste[i] == "[":
        char[1] += 1
    elif liste[i] == "{":
        char[2] += 1
    elif liste[i] == "<":
        char[3] += 1

    elif liste[i] == ")":
        char[0] -= 1
    elif liste[i] == "]":
        char[1] -= 1
    elif liste[i] == "}":
        char[2] -= 1
    elif liste[i] == ">":
        char[3] -= 1
    else:
        print("n again")"""
print(char)
