def start():
    with open('3.txt') as f:
        input = f.readlines()
        
    return input

def checkAround(nr, i, j, input):
    '''this function checks for numbers around the given symbols, and returns them if directly adjacent or diagonal'''
    print("Checking around", nr, "at", i, j)
    numbers = []
    
    # check for numbers around the symbol
    # check for numbers above and below
    for di, dj, direction in [(-1, 0, "above"), (1, 0, "below"), (0, -1, "left"), (0, 1, "right"), (-1, -1, "above left"), (-1, 1, "above right"), (1, -1, "below left"), (1, 1, "below right")]:
        ni, nj = i + di, j + dj
        if 0 <= ni < len(input) and 0 <= nj < len(input[ni]) and input[ni][nj].isdigit():
            number = input[ni][nj]
            while 0 <= ni-di < len(input) and 0 <= nj-dj < len(input[ni-di]) and input[ni-di][nj-dj].isdigit():
                number = input[ni-di][nj-dj] + number
                ni, nj = ni - di, nj - dj
            while 0 <= ni+di < len(input) and 0 <= nj+dj < len(input[ni+di]) and input[ni+di][nj+dj].isdigit():
                number = number + input[ni+di][nj+dj]
                ni, nj = ni + di, nj + dj
            print("Found", number, direction)
            numbers.append(int(number))
        
    return numbers
    
    
   

def ex(input):
    symbols = ['*', '$', '%', '+', '&', '-', '#', '=', '/', '@']
    for i, y in enumerate(input):
        for j, x in enumerate(y):
            if x in symbols:
                print(checkAround(x, i, j, input))
                return 0
            
            
            # print(f"Checking {i}, {j} at {x}, {y}")
    
    return 0

print(ex(start()))