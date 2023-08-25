def is_valid_index(idx, seq):
    return 0 <= idx < len(seq)


pirate_ship = [int(section) for section in input().split(">")]
warship = [int(section) for section in input().split(">")]
max_hp = int(input())

is_running = True
while is_running:
    command = input()
    if command == "Retire":
        break

    com_args = command.split(" ")
    action = com_args[0]
    if action == "Fire":
        idx = int(com_args[1])
        damage = int(com_args[2])
        if not is_valid_index(idx, warship):
            continue
        warship[idx] -= damage
        if warship[idx] <= 0:
            print("You won! The enemy ship has sunken.")
            is_running = False

    elif action == "Defend":
        start_idx = int(com_args[1])
        end_idx = int(com_args[2])
        damage = int(com_args[3])
        if not is_valid_index(start_idx, pirate_ship) or not is_valid_index(end_idx, pirate_ship):
            continue
        for idx in range(start_idx, end_idx+1):
            pirate_ship[idx] -= damage
            if pirate_ship[idx] <= 0:
                is_running = False
                print("You lost! The pirate ship has sunken.")
                break

    elif action == "Repair":
        idx = int(com_args[1])
        hp = int(com_args[2])
        if not is_valid_index(idx, pirate_ship):
            continue
        pirate_ship[idx] = min(max_hp, pirate_ship[idx] + hp)

    elif action == "Status":
        count = [sec for sec in pirate_ship if sec < max_hp * 0.2]
        print(f"{len(count)} sections need repair.")

if is_running:
    print(f"Pirate ship status: {sum(pirate_ship)}")
    print(f"Warship status: {sum(warship)}")