side_by_player = {}
player_by_side = {}

line = input()

while line != "Lumpawaroo":
    if " | " in line:
        force_side, force_user = line.split(" | ")
        if force_side not in player_by_side:
            player_by_side[force_side] = []

        if force_user not in side_by_player:
            side_by_player[force_user] = force_side
            player_by_side[force_side].append(force_user)

    else:
        force_user, force_side = line.split(" -> ")
        if force_side not in player_by_side:
            player_by_side[force_side] = []

        if force_user in side_by_player:
            old_side = side_by_player[force_user]
            player_by_side[old_side].remove(force_user)
            player_by_side[force_side].append(force_user)
            side_by_player[force_user] = force_side

        else:
            side_by_player[force_user] = force_side
            player_by_side[force_side].append(force_user)

        print(f"{force_user} joins the {force_side} side!")

    line = input()

for side in player_by_side:
    if len(player_by_side[side]) > 0:
        print(f"Side: {side}, Members: {len(player_by_side[side])}")
        for player in player_by_side[side]:
            print(f"! {player}")