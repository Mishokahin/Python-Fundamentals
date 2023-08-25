string = input().split(", ")
sheep_count = len(string) - 1
for i in string:
    if i == "wolf" and sheep_count == 0:
        print("Please go away and stop eating my sheep")
    elif i == "wolf":
        print(f"Oi! Sheep number {sheep_count}! You are about to be eaten by a wolf!")

    sheep_count -= 1