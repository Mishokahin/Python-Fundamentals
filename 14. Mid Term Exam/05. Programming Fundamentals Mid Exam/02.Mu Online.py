player_hp = 100
player_bitcoin = 0

rooms = input().split("|")

for index, room in enumerate(rooms):
    command_args = rooms[index].split(" ")
    action = command_args[0]
    if action == "potion":
        potion_amount = int(command_args[1])
        if player_hp + potion_amount > 100:
            potion_amount -= (player_hp + potion_amount) - 100
        player_hp = min(player_hp + potion_amount, 100)
        print(f"You healed for {potion_amount} hp.")
        print(f"Current health: {player_hp} hp.")

    elif action == "chest":
        bitcoins_found = int(command_args[1])
        player_bitcoin += bitcoins_found
        print(f"You found {bitcoins_found} bitcoins.")

    else:
        damage = int(command_args[1])
        monster = action
        player_hp -= damage
        if player_hp <= 0:
            print(f"You died! Killed by {monster}.")
            print(f"Best room: {index+1}")
            exit()
        print(f"You slayed {monster}.")

print("You've made it!")
print(f"Bitcoins: {player_bitcoin}")
print(f"Health: {player_hp}")