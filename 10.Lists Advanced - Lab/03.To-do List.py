notes = [0 for i in range(10)]
command = input()

while command != "End":
    command = command.split("-")
    notes.pop(int(command[0])-1)
    notes.insert(int(command[0])-1, command[1])
    command = input()

print(list([i for i in notes if i != 0]))