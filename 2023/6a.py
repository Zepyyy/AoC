from itertools import islice

def start():
    with open('6.txt') as f:
        input = f.readlines()
    return input
        
def calculateDistance(Time, maxDistance):
    # print("Time: " + str(Time) + " Distance: " + str(maxDistance))
    for hold in range(1, int(Time)+1):
        # if hold <= skip and skip != 0:
        #     continue
        # print("held for " + str(hold) + " ms")
        # print(f"{(int(Time) - hold)*hold} m")
        if (int(Time) - hold)*hold > int(maxDistance): # if the distance is greater than the max distance, skip until it is not (use next())
            # skip = int(Time) - hold
            # print(f"{[i for i in range(hold, int(Time) - hold +1)]} m")
            return ((int(Time) - 2*hold)+ 1)

def ex(input):
    import re
    
    for line in input:
        if line.startswith('Time:'):
            times = re.findall(r'\d+', line)
        elif line.startswith('Distance:'):
            distances = re.findall(r'\d+', line)
    results = 1
    for i in range(len(times)):
        results *= calculateDistance(times[i], distances[i])
    return results


print(ex(start()))