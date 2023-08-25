orders_count = int(input())
total_price = 0

for i in range(orders_count):
    inputs = [float(input()), int(input()), int(input())]
    current_price = 0
    if 0.01 <= inputs[0] <= 100.00 and 1 <= inputs[1] <= 31 and 1 <= inputs[2] <= 2000:
        current_price = inputs[0] * inputs[1] * inputs[2]
        print(f"The price for the coffee is: ${current_price:.2f}")
        total_price += current_price
    else:
        continue

print(f"Total: ${total_price:.2f}")