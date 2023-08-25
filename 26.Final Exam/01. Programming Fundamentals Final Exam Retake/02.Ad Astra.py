import re
import math

text = input()

pattern = r"(#|\|)([a-zA-z\s]+)\1([0-9]{2}/[0-9]{2}/[0-9]{2})\1([0-9]+)\1"

total_calories = 0

matches = re.findall(pattern, text)
items = []

for match in matches:
    item_name = match[1]
    expiration_date = match[2]
    calories = int(match[3])
    total_calories += calories

    items.append(f"Item: {item_name}, Best before: {expiration_date}, Nutrition: {calories}")

days = math.floor(total_calories/2000)
print(f"You have food to last you for: {days} days!")
print("\n".join(items))