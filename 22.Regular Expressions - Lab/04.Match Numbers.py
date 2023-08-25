import re

pattern = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"

sequence = input()

matches = re.finditer(pattern, sequence)

for match in matches:
    print(match.group(), end=" ")