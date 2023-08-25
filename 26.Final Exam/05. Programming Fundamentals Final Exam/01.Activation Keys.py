raw_activation_key = input()

while True:
    command = input()
    if command == "Generate":
        break

    command_args = command.split(">>>")
    action = command_args[0]

    if action == "Contains":
        substring = command_args[1]
        if substring not in raw_activation_key:
            print("Substring not found!")
            continue
        print(f"{raw_activation_key} contains {substring}")
        continue

    if action == "Flip":
        sub_action = command_args[1]
        start_index = int(command_args[2])
        end_index = int(command_args[3])
        if sub_action == "Upper":
            upper = raw_activation_key[start_index:end_index].upper()
            raw_activation_key = raw_activation_key[:start_index] + upper + raw_activation_key[end_index:]
        if sub_action == "Lower":
            lower = raw_activation_key[start_index:end_index].lower()
            raw_activation_key = raw_activation_key[:start_index] + lower + raw_activation_key[end_index:]

    if action == "Slice":
        start_index = int(command_args[1])
        end_index = int(command_args[2])
        substring = raw_activation_key[start_index:end_index]
        raw_activation_key = raw_activation_key.replace(substring, "", 1)

    print(raw_activation_key)

activation_key = raw_activation_key
print(f"Your activation key is: {activation_key}")