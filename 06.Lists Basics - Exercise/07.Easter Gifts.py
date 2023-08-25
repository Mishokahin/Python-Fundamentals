gifts = [i for i in input().split()]
command = input()
while command != "No Money":
    command = command.split()
    if command[0] == "OutOfStock":
        for i in range(len(gifts)):
            if gifts[i] == command[1]:
                gifts[i] = "None"
    if command[0] == "Required":
        gifts[int(command[2])] = command[1]
    if command[0] == "JustInCase":
        gifts[len(gifts)-1] = command[1]

    command = input()

print(*gifts, sep=" ")