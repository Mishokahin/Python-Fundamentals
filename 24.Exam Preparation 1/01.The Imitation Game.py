text = input()

while True:
    command = input()
    if command == "Decode":
        break

    command_args = command.split("|")
    if command_args[0] == "Move":
        beginning_characters = text[:int(command_args[1])]
        end_characters = text[int(command_args[1]):]
        text = end_characters + beginning_characters

    if command_args[0] == "Insert":
        text = text[:int(command_args[1])] + command_args[2] + text[int(command_args[1]):]

    if command_args[0] == "ChangeAll":
        text = text.replace(command_args[1], command_args[2])

message = "".join(text)

print(f"The decrypted message is: {message}")