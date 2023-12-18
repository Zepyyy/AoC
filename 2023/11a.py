def start():
    with open("11.txt", "r") as f:
        input = f.read().strip().split("\n")
        # input = [
        #     "...1......",
        #     ".......2..",
        #     "3.........",
        #     "..........",
        #     "......4...",
        #     ".5........",
        #     ".........6",
        #     "..........",
        #     ".......7..",
        #     "8...9.....",
        # ]  # for testing
    return input


def ex(input):
    nb = []
    expansion = {"x": [], "y": []}
    totalSum = 0
    for y, line in enumerate(input):
        for x, char in enumerate(line):
            if char != ".":
                nb.append((x, y))
        if len(line) == line.count("."):
            expansion["y"].append(y)

    # transpose the input
    second = ["".join([line[i] for line in input]) for i in range(len(input[0]))]

    for y, line in enumerate(second):
        if len(line) == line.count("."):
            expansion["x"].append(y)

    for i in range(len(nb)):
        for j in range(i + 1, len(nb)):
            x = len(
                [
                    x
                    for x in expansion["x"]
                    if nb[j][0] < x < nb[i][0] or nb[j][0] > x > nb[i][0]
                ]
            )
            y = len(
                [
                    y
                    for y in expansion["y"]
                    if nb[j][1] < y < nb[i][1] or nb[j][1] > y > nb[i][1]
                ]
            )

            totalSum += abs((nb[j][0] - nb[i][0])) + abs(nb[j][1] - nb[i][1]) + x + y
    return totalSum


def main():
    return ex(start())


if __name__ == "__main__":
    print(main())
