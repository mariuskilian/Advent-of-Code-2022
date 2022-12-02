# https://adventofcode.com/2022/day/2

# !Part 1
with open('2.txt', 'r') as input:
    score = 0
    for line in input:
        opponent, me = line.removesuffix('\n').split(' ')
        # Normalize both inputs to 0, 1, 2 (Rock, Paper, Scissors)
        opponent = ord(opponent) - ord('A')
        me = ord(me) - ord('X')
        # Extract score
        score += me + 1 + (((me - opponent + 4) * 3) % 9)
    print(score)
    
# !Part 2
with open('2.txt', 'r') as input:
    score = 0
    for line in input:
        opponent, outcome = line.removesuffix('\n').split(' ')
        # Normalize input to 0, 1, 2, make outcome be -1, 0, 1 (Loss, Draw, Win)
        opponent = ord(opponent) - ord('A')
        outcome = ord(outcome) - ord('X') - 1
        me = (opponent + outcome + 3) % 3
        # Extract Score
        score += me + 1 + (((me - opponent + 4) * 3) % 9)
    print(score)