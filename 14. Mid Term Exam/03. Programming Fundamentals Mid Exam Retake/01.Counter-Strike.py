energy = int(input())

battles_won = 0

command = input()

while command != "End of battle":
    distance = int(command)
    if energy < distance:
        print(f"Not enough energy! Game ends with {battles_won} won battles and {energy} energy")
        exit()

    battles_won += 1
    energy -= distance

    if battles_won % 3 == 0:
        energy += battles_won

    command = input()

print(f"Won battles: {battles_won}. Energy left: {energy}")
