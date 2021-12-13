liste = [
    str(i) for i in open("C:\\Users\\quent\\Desktop\\AoC2021\\AoC10.txt", "r").read()
]
print(liste)

char = [0, 0, 0, 0]
for i in range(len(liste) - 1):
    if liste[i] == "(":
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
        print("n again")
print((3 * char[0]) + (57 * char[1]) + (1197 * char[2]) + (25137 * char[3]))
