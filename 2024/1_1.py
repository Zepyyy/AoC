def start():
    with open('./data/1.txt') as f:
        input = f.read().splitlines()
    return input


input = start()

left = [s.split()[0] for s in input]
right = [s.split()[1] for s in input]


def calculate_simularity_score(number, right):
    score = 0
    for i in right:
        if number == i:
            score += 1
    return int(score)*int(number)


def part1(left, right):
    total = 0
    left.sort()
    right.sort()

    total = [calculate_simularity_score(i, right) for i in (left)]
    total = sum(total)

    return total


print(part1(left, right))
