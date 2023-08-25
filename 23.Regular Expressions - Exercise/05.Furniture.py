import re

pattern = r">>([A-z]+)<<(\d+(\.?\d*)?)!(\d+)"

bought_furniture = []
total_price = 0


while True:
    text = input()
    if text == "Purchase":
        break

    match = re.findall(pattern, text)
    if not match:
        continue

    groups = match[0]
    item = groups[0]
    price = float(groups[1])
    quantity = int(groups[3])

    bought_furniture.append(item)
    total_price += price * quantity

print("Bought furniture:")
if bought_furniture:
    print("\n".join(bought_furniture))
print(f"Total money spend: {total_price:.2f}")