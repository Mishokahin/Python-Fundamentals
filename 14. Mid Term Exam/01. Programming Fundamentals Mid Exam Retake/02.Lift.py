people = int(input())
lift = [int(cart) for cart in input().split()]

for idx in range(len(lift)):
    cart_load = min(4 - lift[idx], people)
    lift[idx] += cart_load
    people -= cart_load

if people > 0:
    print(f"There isn't enough space! {people} people in a queue!")

elif len([cart for cart in lift if cart < 4]) > 0:
    print("The lift has empty spots!")

print(*lift)