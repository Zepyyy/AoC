def start():
    with open('3.txt') as f:
        input = f.readlines()
        input = [i.strip() for i in input]
    return input


def checkAround(symbol, x, y, input):
    '''this function checks for numbers around the given symbols, and returns them if directly adjacent or diagonal'''

    result = []

    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if i == x and j == y:
                continue
            elif input[j][i].isdigit():
                nb = input[j][i]
                k = -1
                while input[j][i+k].isdigit() and i+k >= 0:
                    nb += input[j][i+k]
                    input[j] = f"{input[j][:i+k]}.{input[j][i+k+1:]}"
                    k -= 1
                nb = nb[::-1]
                k = 1
                while i+k < len(input[j]) and input[j][i+k].isdigit():
                    nb += input[j][i+k]
                    input[j] = f"{input[j][:i+k]}.{input[j][i+k+1:]}"
                    k += 1
                result.append(int(nb))
    return result


def ex(input):
    result = 0
    a = []
    for y, line in enumerate(input):
        for x, char in enumerate(line):
            if char != "." and not char.isdigit():
                a = checkAround(char, x, y, input)
                # print(a, char)
                if len(a) == 2 and char == "*":
                    result += a[0] * a[1]
                else:
                    # result += sum(a)
                    continue
                # print(f"result: {result}")
    return result


print(ex(start()))
