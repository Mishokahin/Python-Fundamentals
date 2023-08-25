import re
matches = []

while True:
    text = input()
    if not text:
        break
    pattern = r"\d+"
    match = re.findall(pattern, text)
    matches.extend(match)

print(*matches)