inventory = [item for item in input().split(", ")]

while True:
    command = input()
    if command == "Craft!":
        break

    action, item = command.split(" - ")
    if action == "Collect":
        if item not in inventory:
            inventory.append(item)
    elif action == "Drop":
        if item in inventory:
            inventory.remove(item)
    elif action == "Combine Items":
        old_item, new_item = item.split(":")
        if old_item in inventory:
            inventory.insert(inventory.index(old_item)+1, new_item)
    elif action == "Renew":
        if item in inventory:
            inventory.remove(item)
            inventory.append(item)

print(", ".join(inventory))