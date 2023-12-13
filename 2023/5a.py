def start():
    with open('5.txt') as f:
        input = f.read()
    return input


def map(seeds, *category):
    locations = []
    for seed in seeds:
        value = seed
        for i in category:
            for index, j in enumerate(i):
                if int(j[1]) <= int(value) <= int(j[1])+int(j[2]):
                    value = int(j[0])+(int(value)-int(j[1]))
                    break
                elif index != len(i)-1:
                    continue
                else:
                    value=value
                    break
        locations.append(value)
    return min(locations)

def ex(input):
    import re
    # Use regular expressions to find matches in the entire text
    seeds = re.findall(r'seeds: ([\d\s]+)', input)
    soil = re.findall(r'seed-to-soil map:\n([\d\s\n]+)', input)
    fertilizer = re.findall(r'soil-to-fertilizer map:\n([\d\s\n]+)', input)
    water = re.findall(r'fertilizer-to-water map:\n([\d\s\n]+)', input)
    light = re.findall(r'water-to-light map:\n([\d\s\n]+)', input)
    temperature = re.findall(r'light-to-temperature map:\n([\d\s\n]+)', input)
    humidity = re.findall(r'temperature-to-humidity map:\n([\d\s\n]+)', input)
    location = re.findall(r'humidity-to-location map:\n([\d\s\n]+)', input)
    
    # Extract individual numbers from the captured groups
    seeds = re.findall(r'\b\d+\b', ' '.join(seeds))
    soil = [re.findall(r'\b\d+\b', line) for line in soil[0].split('\n') if line.strip()]
    fertilizer = [re.findall(r'\b\d+\b', line) for line in fertilizer[0].split('\n') if line.strip()]
    water = [re.findall(r'\b\d+\b', line) for line in water[0].split('\n') if line.strip()]
    light = [re.findall(r'\b\d+\b', line) for line in light[0].split('\n') if line.strip()]
    temperature = [re.findall(r'\b\d+\b', line) for line in temperature[0].split('\n') if line.strip()]
    humidity = [re.findall(r'\b\d+\b', line) for line in humidity[0].split('\n') if line.strip()]
    location = [re.findall(r'\b\d+\b', line) for line in location[0].split('\n') if line.strip()]

    return map(seeds, soil, fertilizer, water, light, temperature, humidity, location)
    # Add similar print statements for other variables if needed

print(ex(start()))
