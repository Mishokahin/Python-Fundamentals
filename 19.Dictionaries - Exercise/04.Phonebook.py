phonebook = {}

command = input()
while "-" in command:
    name, number = command.split("-")
    if name not in phonebook:
        phonebook[name] = 0
    phonebook[name] = number

    command = input()

n = int(command)

for i in range(int(n)):
    name = input()
    if name in phonebook:
        print(f"{name} -> {phonebook[name]}")
    else:
        print(f"Contact {name} does not exist.")