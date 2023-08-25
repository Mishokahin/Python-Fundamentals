import math
numbers = input().split(", ")
beggars = int(input())
beggars_income = [0 for i in range(beggars)]
beggars_turns = [[i for i in range(beggars)] for i in range(math.ceil(len(numbers)/beggars))]
beggars_position = [word for words in beggars_turns for word in words]

for i in range(len(numbers)):
    beggars_income[beggars_position[i]] += int(numbers[i])

print(beggars_income)