travel_plan = input()

while True:
    changes = input()
    if changes == "Travel":
        break

    command_args = changes.split(":")
    command = command_args[0]
    if command == "Add Stop":
        index = int(command_args[1])
        string = command_args[2]
        travel_plan = travel_plan[:index] + string + travel_plan[index:]
        print(travel_plan)

    if command == "Remove Stop":
        start_index = int(command_args[1])
        end_index = int(command_args[2])
        if start_index in range(0, len(travel_plan)) and end_index in range(0, len(travel_plan)):
            travel_plan = travel_plan[:start_index] + travel_plan[end_index+1:]
        print(travel_plan)

    if command == "Switch":
        old_string = command_args[1]
        new_string = command_args[2]
        travel_plan = travel_plan.replace(old_string, new_string)
        print(travel_plan)

print(f"Ready for world tour! Planned stops: {travel_plan}")