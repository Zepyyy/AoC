import re

def start():
    with open('7.txt') as f:
        input = f.readlines()
    return input

def ex(input):
    three = ""
    print(input[-1])
    three = re.findall(r'(?<!\w)(\w)(?!(?:.*\1){3})(?=(?:.*\1){2}.*\b\1\b).*$', input[-1])
    return three

print(ex(start()))