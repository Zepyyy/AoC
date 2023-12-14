def start():
    with open('8.txt') as f:
        input = f.read().strip().split('\n')
        # input = ['LR', '11A = (11B, XXX)', '11B = (XXX, 11Z)', '11Z = (11B, XXX)', '22A = (22B, XXX)', '22B = (22C, 22C)', '22C = (22Z, 22Z)', '22Z = (22B, 22B)', 'XXX = (XXX, XXX)']
    return input

def setting(nb, navNode, instructions, nodes, navNodes):
    # print(f"just setting, nb: {nb}, navNode: {navNode}")
    while navNode[-1] != 'Z' or nb != 0:
        for inst in instructions:
            nb += 1
            index = nodes.index(navNode)
            if inst == 'L':
                navNode = navNodes[index].split(', ')[0]
            else:
                navNode = navNodes[index].split(', ')[1]
            if navNode[-1] == 'Z':
                # print(f"at: {nb}, stopped at: {navNode}")
                return nb, navNode

def Navigate(prevNB, navNode, instructions, nodes, navNodes):
    # print(f"----trying node: {navNode}, stopping at: {prevNB}----")
    nb = 0
    while True:
        for inst in instructions:
            nb += 1            
            index = nodes.index(navNode)
            if inst == 'L':
                navNode = navNodes[index].split(', ')[0]
            else:
                navNode = navNodes[index].split(', ')[1]
            if nb == prevNB:
                print(f"at: {nb}, stopped at: {navNode}, found?: {navNode[-1] == 'Z'}")
                return nb, navNode[-1] == 'Z'

def ex(input):
    instructions = input[0]
    lines = [i for i in input[1:] if '=' in i]

    nodes = [lines.split(' = ')[0] for lines in lines]
    navNodes = [lines.split(' = ')[1].strip('()') for lines in lines]
    startNodes = [i for i in nodes if i[-1]=='A']
    print(f"startNodes: {startNodes}")
    nb = 0
    found = False
    oe = 1
    stopNode = startNodes[0]
    while True:
        
        nb, stopNode = setting(nb, stopNode, instructions, nodes, navNodes)
        for node in startNodes[1:]:
            prevNB, found = Navigate(nb, node, instructions, nodes, navNodes)
            if found:
                oe += 1
                continue
            else:
                nb = prevNB
                break
        if oe >= len(startNodes):
            return nb
        else:
            None
            # print(f"oe: {oe}, len(startNodes): {len(startNodes)}")
            # return 0
             
        
    return nb


print(ex(start()))
