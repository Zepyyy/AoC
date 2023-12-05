liste = open('1.txt').readlines()

sum = 0
nbs = ['one','two','three','four','five','six','seven','eight','nine']

for i in liste:
    hi = ''
    for k in range(0, len(i)-1, 1):
        if hi != '':
            break
        if i[k].isdigit():
            hi += str(i[k])
        else:
            for qsd in nbs:
                if qsd in i[:k+1]:
                    hi += str(nbs.index(qsd)+1)
            
    for k in range(len(i)-1, 0, -1):
        if len(hi) > 1:
            break
        if i[k].isdigit():
            hi += str(i[k])
        else:
            for qsd in nbs:
                # print("qsd loop")
                if qsd in i[k-1:]:
                    hi += str(nbs.index(qsd)+1)
    sum += int(hi) if len(hi) > 1 else int(str(hi)+str(hi))
print("sum",sum)
