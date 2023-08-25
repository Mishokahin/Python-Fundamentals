words = [letter for letter in input() if letter != " "]

char_occurrences = {}

for char in words:
    if char not in char_occurrences:
        char_occurrences[char] = 0
    char_occurrences[char] += 1

for char, occurrences in char_occurrences.items():
    print(f"{char} -> {occurrences}")