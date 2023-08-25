import re

pairs = []

text = input()

pattern = r"(@|#)([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1"

matches = re.findall(pattern, text)
for match in matches:
    pairs.append([match[1], match[2]])

mirror_pairs = []
if not pairs:
    print("No word pairs found!")
else:
    print(f"{len(pairs)} word pairs found!")

for pair in pairs:
    mirror = pair[0][::-1]
    if pair[1] == mirror:
        mirror_pairs.append(f"{pair[0]} <=> {pair[1]}")

if not mirror_pairs:
    print("No mirror words!")
else:
    print("The mirror words are:")
    print(", ".join(mirror_pairs))