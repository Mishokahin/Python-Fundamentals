def order(item, count):
    price = None
    if item == "coffee":
        price = count * 1.5
    elif item == "coke":
        price = count * 1.4
    elif item == "water":
        price = count * 1.0
    elif item == "snacks":
        price = count * 2.0
    return price


print(f"{order(input(), int(input())):.2f}")