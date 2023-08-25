concealed_message = input()

while True:
    line = input()
    if line == "Reveal":
        break

    command_args = line.split(":|:")
    action = command_args[0]

    if action == "InsertSpace":
        index = int(command_args[1])
        concealed_message = concealed_message[:index] + " " + concealed_message[index:]

    if action == "Reverse":
        substring = command_args[1]
        if substring not in concealed_message:
            print("error")
            continue
        else:
            concealed_message = concealed_message.replace(substring, "", 1)
            concealed_message = concealed_message + substring[::-1]

    if action == "ChangeAll":
        substring, replacement = command_args[1], command_args[2]
        concealed_message = concealed_message.replace(substring, replacement)

    print(concealed_message)

print(f"You have a new text message: {concealed_message}")