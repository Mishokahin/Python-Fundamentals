import re
text = input()

pattern = r"(\@{1,}|\#{1,})([a-z]{3,})(\@{1,}|\#{1,})([^A-Za-z0-9]*?)(\/)(\d+)(\/)"

matches = re.findall(pattern, text)

for match in matches:
    amount = match[5]
    color = match[1]
    print(f"You found {amount} {color} eggs!")