wagon_count = int(input())
train = [0 for i in range(wagon_count)]
command = input()

while command != "End":
    command = command.split()
    if command[0] == "add":
        train[wagon_count-1] += int(command[1])
    if command[0] == "insert":
        train[int(command[1])] += int(command[2])
    if command[0] == "leave":
        train[int(command[1])] -= int(command[2])

    command = input()

print(train)