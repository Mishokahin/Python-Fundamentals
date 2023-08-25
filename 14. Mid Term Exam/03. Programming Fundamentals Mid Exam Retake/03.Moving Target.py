targets = [int(target) for target in input().split()]

line = input()

while line != "End":
    command_args = line.split()
    command = command_args[0]
    if command == "Shoot":
        idx = int(command_args[1])
        power = int(command_args[2])
        if idx in range(len(targets)):
            targets[idx] -= power
            if targets[idx] <= 0:
                del targets[idx]

    elif command == "Add":
        idx = int(command_args[1])
        value = int(command_args[2])
        if idx in range(len(targets)):
            targets.insert(idx, value)
        else:
            print("Invalid placement!")

    elif command == "Strike":
        idx = int(command_args[1])
        radius = int(command_args[2])
        idx1 = idx - radius
        idx2 = idx + radius
        if idx1 in range(len(targets)) and idx2 in range(len(targets)):
            del targets[idx1:idx2+1]
        else:
            print("Strike missed!")

    line = input()

print(f"{'|'.join(str(target) for target in targets)}")