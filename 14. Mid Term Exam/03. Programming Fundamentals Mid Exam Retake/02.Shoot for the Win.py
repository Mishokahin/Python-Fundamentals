targets = [int(target) for target in input().split()]

command = input()

while command != "End":
    idx = int(command)
    if idx in range(len(targets)):
        current_target = targets[idx]
        for i in range(len(targets)):
            if targets[i] > current_target and targets[i] != -1:
                targets[i] -= current_target
            elif targets[i] <= current_target and targets[i] != -1:
                targets[i] += current_target
        targets[idx] = -1

    command = input()

print(f"Shot targets: {targets.count(-1)} -> {' '.join(str(target) for target in targets)}")