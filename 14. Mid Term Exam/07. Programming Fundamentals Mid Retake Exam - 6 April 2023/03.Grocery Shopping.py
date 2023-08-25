shopping_list = [prod for prod in input().split("|")]

command = input().split("%")

while command != "Shop!":
    action = command[0]
    if action == "Important":
        product = command[1]
        if product not in shopping_list:
            shopping_list.insert(0, product)
        else:
            shopping_list.remove(product)
            shopping_list.insert(0, product)
    if action == "Add":
        product = command[1]
        if product in shopping_list:
            print("The product is already in the list.")
        else:
            shopping_list.append(product)
    if action == "Swap":
        product1, product2 = command[1], command[2]
        if product1 not in shopping_list:
            print(f"Product {product1} missing!")
        elif product2 not in shopping_list:
            print(f"Product {product2} missing!")
        else:
            product1_idx = shopping_list.index(product1)
            product2_idx = shopping_list.index(product2)
            shopping_list[product1_idx], shopping_list[product2_idx] = product2, product1

    if action == "Remove":
        product = command[1]
        if product not in shopping_list:
            print(f"Product {product} isn't in the list.")
        else:
            shopping_list.remove(product)

    if action == "Reversed":
        shopping_list.reverse()

    if action == "Shop!":
        break

    command = input().split("%")

for pr in range(len(shopping_list)):
    print(f"{pr+1}. {shopping_list[pr]}")