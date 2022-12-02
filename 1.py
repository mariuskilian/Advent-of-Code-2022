# https://adventofcode.com/2022/day/1

# !Part 1
with open('1.txt', 'r') as input:
    totalCalories = [0]
    for line in input:
        if (line is not '\n'): totalCalories[-1] += int(line)
        else: totalCalories += [0]
    print(max(totalCalories))

# !Part 2
totalCalories.sort(reverse=True);
print(sum(totalCalories[:3]))