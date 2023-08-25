loses_count = int(input())
helmet = [float(input()), 0]
sword = [float(input()), 0]
shield = [float(input()), 0]
armor = [float(input()), 0]

for fight in range(1, loses_count+1):
    if fight % 2 == 0:
        helmet[1] += 1
    if fight % 3 == 0:
        sword[1] += 1
    if fight % 3 == 0 and fight % 2 == 0:
        shield[1] += 1
        if shield[1] % 2 == 0:
            armor[1] += 1

expenses = sum([helmet[0] * helmet[1], sword[0] * sword[1], shield[0] * shield[1], armor[0] * armor[1]])

print(f"Gladiator expenses: {expenses:.2f} aureus")