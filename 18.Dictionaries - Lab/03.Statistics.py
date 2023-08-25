products = {}

command = input()
while command != "statistics":
    product, quantity = command.split(": ")
    if product not in products:
        products[product] = int(quantity)
    else:
        products[product] += int(quantity)

    command = input()

print("Products in stock:")
print(f"- {product}: {quantity}" for product, quantity in products.items())
print(f"Total Products: {len(products.keys())}")
print(f"Total Quantity: {sum(products.values())}")