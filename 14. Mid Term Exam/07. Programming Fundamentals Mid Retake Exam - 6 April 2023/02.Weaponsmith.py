name = [particle for particle in input().split("|")]

while True:
    command = input()
    if command == "Done":
        break
    command_args = command.split()
    action = command_args[0]
    if action == "Add":
        idx = int(command_args[2])
        if idx in range(len(name)):
            particle = command_args[1]
            name.insert(idx, particle)
    if action == "Remove":
        idx = int(command_args[1])
        if idx in range(len(name)):
            name.pop(idx)
    if action == "Check":
        even_odd = command_args[1]
        if even_odd == "Even":
            print(" ".join([name[i] for i in range(len(name)) if i % 2 == 0]))
        if even_odd == "Odd":
            print(" ".join([name[i] for i in range(len(name)) if i % 2 != 0]))

print(f"You crafted {''.join(name)}!")