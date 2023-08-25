treasure_chest = [item for item in input().split("|")]

while True:
    command = input()
    if command == "Yohoho!":
        break

    command_args = command.split()
    action = command_args[0]
    if action == "Loot":
        items = [item for item in command_args[1:len(command_args)]]
        for item in items:
            if item not in treasure_chest:
                treasure_chest.insert(0, item)

    elif action == "Drop":
        idx = int(command_args[1])
        if idx in range(len(treasure_chest)):
            item = treasure_chest[idx]
            treasure_chest.remove(item)
            treasure_chest.append(item)

    elif action == "Steal":
        idx = int(command_args[1])
        idx1 = len(treasure_chest) - idx
        idx2 = len(treasure_chest)
        if idx1 not in range(idx2):
            idx1 = 0
        stolen_items = [item for item in treasure_chest[idx1:idx2]]
        print(", ".join(stolen_items))
        del treasure_chest[idx1:idx2]

if len(treasure_chest) == 0:
    print("Failed treasure hunt.")

else:
    item_prices = [len(item) for item in treasure_chest]
    average_gain = sum(item_prices) / len(treasure_chest)
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")