products = input().split(" ")
store = {products[i]: int(products[i+1]) for i in range(0, len(products), 2)}
product = input().split(" ")

for product in product:
    if product in store:
        print(f"We have {store[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")