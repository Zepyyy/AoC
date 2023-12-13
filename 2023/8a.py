def start():
    with open('8.txt') as f:
        input = f.read().strip().split('\n')
        # input = ['RL', 'AAA = (BBB, BBB)', 'BBB = (ZZZ, ZZZ)']
    return input


def Navigate(instructions, nodes):
    print(instructions)
    print(nodes)


def ex(input):
    instructions = input[0]
    lines = [i for i in input[1:] if '=' in i]

    nodes = [lines.split(' = ')[0] for lines in lines]
    navNodes = [lines.split(' = ')[1] for lines in lines]

    print(instructions)
    print(nodes, navNodes)
    Navigate(instructions, nodes)
    return 0


print(ex(start()))
