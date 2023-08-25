prices = [2, 5, 3, 15]
points = [5, 3, 10, 17]
quantity = int(input())
days = int(input())
budget = 0
total_spirit = 0

for i in range(1, days+1):
    tree_set = False
    if i % 11 == 0:
        quantity += 2
    if i % 2 == 0:
        budget += prices[0] * quantity
        total_spirit += points[0]
    if i % 3 == 0:
        budget += (prices[1] + prices[2]) * quantity
        total_spirit += points[1] + points[2]
        tree_set = True
    if i % 5 == 0:
        budget += prices[3] * quantity
        total_spirit += points[3]
        if tree_set is True:
            total_spirit += 30
    if i % 10 == 0:
        budget += prices[1] + prices[2] + prices[3]
        total_spirit -= 20
if days % 10 == 0:
    total_spirit -= 30

print(f"Total cost: {budget}")
print(f"Total spirit: {total_spirit}")