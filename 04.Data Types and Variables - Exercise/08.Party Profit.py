companions_count, days = int(input()), int(input())
coins = 0

for i in range(1, days + 1):
    motivational_party = False
    if i % 10 == 0:
        companions_count -= 2
    if i % 15 == 0:
        companions_count += 5
    coins += 50 - (companions_count * 2)
    if i % 3 == 0:
        coins -= (companions_count * 3)
        motivational_party = True
    if i % 5 == 0:
        coins += companions_count * 20
        if motivational_party:
            coins -= (companions_count * 2)

print(f"{companions_count} companions received {int(coins/companions_count)} coins each.")