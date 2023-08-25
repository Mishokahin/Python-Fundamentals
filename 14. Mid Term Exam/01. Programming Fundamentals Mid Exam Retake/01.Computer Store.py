total_price_without_taxes = 0
is_special = False

while True:
    command = input()
    if command == "regular":
        break
    elif command == "special":
        is_special = True
        break

    part_price = float(command)
    if part_price < 0:
        print("Invalid price!")
    else:
        total_price_without_taxes += part_price

if total_price_without_taxes == 0:
    print("Invalid order!")

else:
    taxes = total_price_without_taxes * 0.2
    total_price_with_taxes = total_price_without_taxes + taxes
    if is_special:
        total_price_with_taxes -= (total_price_with_taxes * 0.1)
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_price_without_taxes:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {total_price_with_taxes:.2f}$")