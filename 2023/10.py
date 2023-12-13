def start():
    with open('10.txt') as f:
        input = f.readlines()
        input = [".....",
                 ".S|7.",
                 ".|.|.",
                 ".L-J.",
                 "....."]
        input = [list(i.strip()) for i in input]
    return input

def move(x, y, nr, input):
    if input[y][x] == "0":
        print("debut.")
        return 1
    else:
        input[y][x] = str(nr)
        return 0
    # input[line][index] = str(nr)

def lookAround(index,line,input):
    nr = 0
    last = 0
    start = [index,line]
    print("start",start)
    for y in range(line-1,line+2):
        for x in range(index-1,index+2):
            if (line - 1 == y and (input[y][x] == "|" or input[y][x] == "7" or input[y][x] == "F")) or (line + 1 == y and (input[y][x] == "|" or input[y][x] == "L" or input[y][x] == "J")) or (index + 1 == x and (input[y][x] == "-" or input[y][x] == "J" or input[y][x] == "7")) or (index - 1 == x and (input[y][x] == "-")):
                if last:
                    return 1
                else:
                    last = move(x,y,nr,input)
                    nr += 1
                    print("nr",nr,"x",x,"y",y)
                    for line in input:
                        print(line)
                    lookAround(x,y,input)
            else:
                continue
    return 0
            
def ex(input):
    for line,y in enumerate(input):
        for index,x in enumerate(y):
            if x == "S":
                print("S",index,line)
                lookAround(index,line,input)
                break
    print("end")
    for line in input:
        print(line)
    return 0

print(ex(start()))