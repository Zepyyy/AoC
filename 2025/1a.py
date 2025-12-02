def start():
    with open("2025/1.txt", "r") as f:
        input = f.read().splitlines()
        return input


def ex(input):
    total = 50
    end = 0
    print("Dial starts by pointing at", total)

    for line in input:
        if line[0] == "L":
            total -= int(line[1:])
        if line[0] == "R":
            total += int(line[1:])

        while total < 0:
            total = 100 + total
        while total >= 100:
            total = total - 100

        print("The dial is rotated", line, "to", total)

        if total == 0:
            end += 1
            # print("YAYAYAYYAY:", end)
    return end


def main():
    input = start()
    print(ex(input))


if __name__ == "__main__":
    main()
