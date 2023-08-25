import re

text = input()

cool_threshold_pattern = r"\d"
cool_threshold_matches = re.findall(cool_threshold_pattern, text)
cool_threshold = 1

for num in cool_threshold_matches:
    cool_threshold *= int(num)

emoji_pattern = r"(:{2}|\*{2})([A-Z][a-z]{2,})\1"
found_emojies = re.findall(emoji_pattern, text)

print(f"Cool threshold: {cool_threshold}")
print(f"{len(found_emojies)} emojis found in the text. The cool ones are:")
for emoji in found_emojies:
    cool_factor = sum([ord(char) for char in emoji[1]])
    if cool_factor >= cool_threshold:
        print(emoji[0]+emoji[1]+emoji[0])