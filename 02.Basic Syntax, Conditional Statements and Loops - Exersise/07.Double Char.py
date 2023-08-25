command = input()

while command != "End":
    if command != "SoftUni":
        double_char = [i * 2 for i in command]
        print(*double_char, sep="")

    command = input()