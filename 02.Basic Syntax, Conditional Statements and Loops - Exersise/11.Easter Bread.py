import math
budget = float(input())
price_of_flour = float(input())
prices = {"flour": price_of_flour, "eggs": price_of_flour * 0.75, "milk": price_of_flour * 1.25}
one_loaf = prices[str("flour")] + prices[str("eggs")] + (prices[str("milk")]/4)
number_of_loaves = 0
colored_eggs = 0

for bread in range(1, math.floor(budget/one_loaf)+1):
    number_of_loaves += 1
    colored_eggs += 3
    if number_of_loaves % 3 == 0:
        colored_eggs -= (number_of_loaves - 2)

money_left = budget % one_loaf
print(f"You made {number_of_loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and"
      f" {money_left:.2f}BGN left.")