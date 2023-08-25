shopping_list = input().split("!")
command = input()

while command != "Go Shopping!":
    token = command.split(" ")
    if token[0] == "Urgent":
        if token[1] not in shopping_list:
            shopping_list.insert(0, token[1])
        pass
    if token[0] == "Unnecessary":
        if token[1] in shopping_list:
            shopping_list.remove(token[1])
        pass
    if token[0] == "Correct":
        if token[1] in shopping_list:
            shopping_list[shopping_list.index(token[1])] = token[2]
        pass
    if token[0] == "Rearrange":
        if token[1] in shopping_list:
            shopping_list.remove(token[1])
            shopping_list.append(token[1])
        pass

    command = input()

print(", ".join(shopping_list))
