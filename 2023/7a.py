import re
from collections import Counter

from numpy import sort

debug = False


def start():
    with open('7.txt') as f:
        input = f.readlines()
    return input


def calculate(finalList):
    result = 0
    for i, j in enumerate(finalList):
        print(f"{int(i+1)} * {int(j)} = {int(i+1)*int(j)}") if debug == True else None
        result += int(i+1)*int(j)
    return result


def ReOrder(hands):
    Strength = ["A", "K", "Q", "J", "T", "9",
                "8", "7", "6", "5", "4", "3", "2"]
    converted = []
    secondList = {}
    kkkkk = 0
    finalList = []
    for i in hands.values():
        if len(i) == 0:
            continue
        kkkkk += 1
        for y in i:
            print("y:", y.split(" ")[0]) if debug == True else None
            value = y.split(" ")[1]
            for z in y.split(" ")[0]:
                converted.append(Strength.index(z))

            print("converted", [l for l in converted]
                  ) if debug == True else None
            print("value", value) if debug == True else None

            secondList[value+"_"+str(''.join([str(l) for l in converted]))
                       ] = converted
            converted = []
        secondList = dict(
            sorted(secondList.items(), key=lambda item: item[1]))
        print(
            f"{(list(hands.keys())[kkkkk-1])}: :{secondList}") if debug == True else None
        finalList.append([roh.split("_")[0] for roh in secondList.keys()])
        secondList = {}

    return [s for s in finalList]


def ex(input):
    Five = []
    Four = []
    FullHouse = []
    Three = []
    Two = []
    One = []
    HighCard = []

    for line in input:
        line = line.strip("\n")
        chars = re.findall(r'.', line.split(" ")[0])

        counts = Counter(chars)
        print([char for char in counts.values()]
              ) if debug == True else None
        if [char for char in counts.values()] == [5]:
            Five.append(line)
        elif [char for char in counts.values()] == [4, 1] or [char for char in counts.values()] == [1, 4]:
            Four.append(line)
        elif [char for char in counts.values()] == [3, 2] or [char for char in counts.values()] == [2, 3]:
            FullHouse.append(line)
        elif [char for char in counts.values()] == [3, 1, 1] or [char for char in counts.values()] == [1, 3, 1] or [char for char in counts.values()] == [1, 1, 3]:
            Three.append(line)
        elif [char for char in counts.values()] == [2, 2, 1] or [char for char in counts.values()] == [2, 1, 2] or [char for char in counts.values()] == [1, 2, 2]:
            Two.append(line)
        elif [char for char in counts.values()] == [2, 1, 1, 1] or [char for char in counts.values()] == [1, 2, 1, 1] or [char for char in counts.values()] == [1, 1, 2, 1] or [char for char in counts.values()] == [1, 1, 1, 2]:
            One.append(line)
        elif [char for char in counts.values()] == [1, 1, 1, 1, 1]:
            HighCard.append(line)
        else:
            print("problem")
    Hands = {"Five": Five, "Four": Four, "FullHouse": FullHouse,
             "Three": Three, "Two": Two, "One": One, "HighCard": HighCard}

    OneHand = ReOrder(Hands)

    OneHand = [item for sublist in OneHand for item in sublist]
    OneHand.reverse()

    print(OneHand) if debug == True else None

    return calculate(OneHand)


print(ex(start()))
