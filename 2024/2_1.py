def start():
    with open('./data/2.txt') as f:
        input = f.readlines()
        return input


input = start()

input = [input.split() for input in input]


def evaluate_safety(line):
    count = 0
    # Either all decreasing or all increasing
    # Adjacent levels differ by 1, 2 or 3

    direction = "decreasing" if int(
        line[1]) - int(line[0]) < 0 else "increasing"

    for i in range(len(line)):
        if i == len(line) - 1:
            count += 1
            return count
        elif abs(int(line[i]) - int(line[i + 1])) > 3:
            return 0
        elif abs(int(line[i]) - int(line[i + 1])) < 1:
            return 0

        if direction == "decreasing" and int(line[i+1]) - int(line[i]) > 0:
            return 0
        elif direction == "increasing" and int(line[i+1]) - int(line[i]) < 0:
            return 0
        else:
            continue


def part1():
    total = 0
    for line in input:
        total += evaluate_safety(line)
    print(total)


part1()
