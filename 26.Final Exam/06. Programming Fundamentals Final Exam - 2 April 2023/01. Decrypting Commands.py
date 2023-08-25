text = input()

while True:
    command = input()
    if command == "Finish":
        break

    command_args = command.split()
    action = command_args[0]

    if action == "Replace":
        current_char = command_args[1]
        new_char = command_args[2]
        text = text.replace(current_char, new_char)
        print(text)

    if action == "Cut":
        start_index = int(command_args[1])
        end_index = int(command_args[2])
        if start_index not in range(len(text)) or end_index not in range(len(text)):
            print("Invalid indices!")
        else:
            sub_string = text[start_index:end_index+1]
            text = text.replace(sub_string, "", 1)
            print(text)

    if action == "Make":
        sub_action = command_args[1]
        if sub_action == "Upper":
            text = text.upper()
            print(text)
        if sub_action == "Lower":
            text = text.lower()
            print(text)

    if action == "Check":
        sub_string = command_args[1]
        if sub_string not in text:
            print(f"Message doesn't contain {sub_string}")
        else:
            print(f"Message contains {sub_string}")

    if action == "Sum":
        start_index = int(command_args[1])
        end_index = int(command_args[2])
        if start_index not in range(len(text)) or end_index not in range(len(text)):
            print("Invalid indices!")
        else:
            sub_string = text[start_index:end_index+1]
            sum_of_substring = sum([ord(char) for char in sub_string])
            print(sum_of_substring)