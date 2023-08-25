numbers = [int(number) for number in input().split()]

while True:
    line = input()
    if line == "end":
        break
    command_args = line.split()
    command = command_args[0]

    if command == "swap":
        idx1 = int(command_args[1])
        idx2 = int(command_args[2])
        numbers[idx1], numbers[idx2] = numbers[idx2], numbers[idx1]

    elif command == "multiply":
        idx1 = int(command_args[1])
        idx2 = int(command_args[2])
        numbers[idx1] = numbers[idx1] * numbers[idx2]

    elif command == "decrease":
        for idx in range(len(numbers)):
            numbers[idx] -= 1

print(*numbers, sep=', ')