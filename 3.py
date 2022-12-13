# https://adventofcode.com/2022/day/3

# ! Part 1
priority = lambda c: (p := ord(c)-ord('a')+1) + (ord('z')-ord('A')+1 if p < 0 else 0)

with open('3.txt', 'r') as input:
    result = 0
    for line in input:
        half = len(line[:-1])//2
        comp1, comp2 = line[:half], line[half:]
        result += [priority(i) for i in comp1 if i in comp2][0]
    print(result)

# ! Part 2
with open('3.txt', 'r') as input:
    result = 0
    lines = input.readlines()
    for group in range(len(lines)//3):
        result += [priority(i) for i in lines[3*group+0] if i in lines[3*group+1] and i in lines[3*group+2]][0]
    print(result)