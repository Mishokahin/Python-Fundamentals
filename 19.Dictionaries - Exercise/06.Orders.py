items = {}
items_quantity = {}
command = input()

while command != "buy":
    command_args = command.split()
    name = command_args[0]
    price = float(command_args[1])
    quantity = int(command_args[2])

    items[name] = price
    if name in items:
        items_quantity[name] += quantity

    else:
        items_quantity[name] = quantity

    command = input()

for item in items:
    total_price = items[item] * items_quantity[item]
    print(f"{item} -> {total_price:.2f}")