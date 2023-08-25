maximum_price = {'Clothes': 50.00, 'Shoes': 35.00, 'Accessories': 20.50}
items_list = input().split("|")
budget = float(input())
items = [str(i).split("->") for i in items_list]
items_bought = []
for i in range(len(items)):
    if str(items[i][0]) in maximum_price and float(items[i][1]) <= maximum_price[str(items[i][0])]:
        if float(items[i][1]) <= budget:
            budget -= float(items[i][1])
            items_bought.append(float(items[i][1]))

new_prices = [float(i) * 1.4 for i in items_bought]
profit = sum(new_prices) - sum(items_bought)
print(' '.join(f"{price:.2f}" for price in new_prices))
print(f"Profit: {profit:.2f}")
if sum(new_prices) + budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")