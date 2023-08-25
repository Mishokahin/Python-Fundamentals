neighborhood = [int(neighbor) for neighbor in input().split("@")]

house_index = 0

while True:
    command = input()
    if command == "Love!":
        break

    jump, idx = command.split()
    if house_index + int(idx) in range(len(neighborhood)):
        house_index += int(idx)
    else:
        house_index = 0

    if neighborhood[house_index] == 0:
        print(f"Place {house_index} already had Valentine's day.")
    else:
        neighborhood[house_index] -= 2
        if neighborhood[house_index] == 0:
            print(f"Place {house_index} has Valentine's day.")


print(f"Cupid's last position was {house_index}.")
houses_failed = len(neighborhood) - neighborhood.count(0)
if houses_failed > 0:
    print(f"Cupid has failed {houses_failed} places.")
else:
    print("Mission was successful.")