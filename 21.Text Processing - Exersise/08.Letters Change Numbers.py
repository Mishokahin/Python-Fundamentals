import string
strings = [s.strip() for s in input().split()]
upper_cases = list(string.ascii_uppercase)

result = 0

for idx in range(len(strings)):
    first_letter = strings[idx][0]
    number = int(strings[idx][1:-1])
    last_letter = strings[idx][-1]
    medium = 0
    if first_letter.isupper():
        medium = number / (upper_cases.index(first_letter) + 1)
    else:
        medium = number * (upper_cases.index(first_letter.upper()) + 1)

    if last_letter.isupper():
        medium -= (upper_cases.index(last_letter) + 1)
    else:
        medium += (upper_cases.index(last_letter.upper()) + 1)

    result += medium

print(f"{result:.2f}")