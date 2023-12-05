import re

def start():
    with open('2.txt') as f:
        input = f.readlines()
        # input = ["Game 23: 1 red, 2 blue; 1 blue, 1 green; 1 green; 3 red, 1 blue, 1 green",
                #  "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"]
        # input = ["Game 80: 13 red, 1 green; 15 red, 1 blue; 8 red, 1 green"]
    return input

def ex(input):
    colors = ["red", "green", "blue"]
    result = 0
    
    for i in input:
        i = i.split(": ")[1].split("; ")
        power = 1
        for color in colors:
            match = [re.findall(r'(\d{1,2})\D*'+color, i) for i in i if color in i]
            least = max([int(''.join(k)) for k in match] or [0])
            power *= least
        result += power
        
    return result

print(ex(start()))