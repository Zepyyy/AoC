def start():
    with open('8.txt') as f:
        input = f.read().strip().split('\n')
        # input = ['LLR', 'AAA = (BBB, BBB)', 'BBB = (AAA, ZZZ)', 'ZZZ = (ZZZ, ZZZ)']
    return input

def ex(input):
    instructions = input[0]
    lines = [i for i in input[1:] if '=' in i]

    nodes = [lines.split(' = ')[0] for lines in lines]
    navNodes = [lines.split(' = ')[1].strip('()') for lines in lines]
    navNode = 'AAA'
    nb = 0
    while navNode != 'ZZZ':
        for inst in instructions:
            nb += 1            
            index = nodes.index(navNode)
            if inst == 'L':
                navNode = navNodes[index].split(', ')[0]
            else:
                navNode = navNodes[index].split(', ')[1]
            if navNode == 'ZZZ':
                return nb
    return 0


print(ex(start()))
