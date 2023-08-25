events_lowercase = ["coding", "dog", "cat", "movie"]
events_uppercase = [i.upper() for i in events_lowercase]
coffee_count = 0
event = input()

while event != "END":
    if event in events_lowercase:
        coffee_count += 1
    if event in events_uppercase:
        coffee_count += 2

    if coffee_count > 5:
        print("You need extra sleep")
        exit()

    event = input()

print(coffee_count)