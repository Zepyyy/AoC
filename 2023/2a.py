import re

def start():
    with open('2.txt') as f:
        input = f.readlines()
        input = ["Game 5: 1 red, 1 blue, 3 green; 2 blue, 1 red, 2 green; 5 blue, 3 red, 16 green"]
    return input

def ex(input):
    max = {"red": 12, "green": 13, "blue": 14}
    colors = ["red", "green", "blue"]
    result = 0
    
    for i in input:
        nr = int(re.findall(r'(\d{1,2})\s*:', i)[0])
        print(nr)
        i = i.split(": ")[1].split("; ")
        good = True
        
        for color in colors:
            match = [re.findall(r'(\d{1,2})\D*'+color, i) for i in i if color in i]
            for k in range(len(match)):
                if not max[color] >= int(match[k][0]):
                    print(f"{color} not good so {nr} is not good")
                    good = False
                    break
                else:
                    continue
        
        # print(nr, "is good")
        if good:
            result +=int(nr)
    
        
    return result

print(ex(start()))