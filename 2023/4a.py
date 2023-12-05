def start():
    with open('4.txt') as f:
        input = f.read().splitlines()
        # input = ["Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53", "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19"]
    return input


def ex(input):
    import re
    result = 0
    for line in input:
        # Extract the part of the line after the colon
        numbers_part = line.split(":")[1]

        # Split the numbers part at the pipe
        left_side, right_side = numbers_part.split('|')

        # Use regex to get the numbers from each side
        left_numbers = re.findall(r'\d+', left_side)
        right_numbers = re.findall(r'\d+', right_side)
        
        inter = list(set(left_numbers) & set(right_numbers))
        result += 2**(len(inter)-1) if len(inter) > 0 else 0
        
    return result
print(ex(start()))