liked_meals = {}
dislike_meals = {}

while True:
    command = input()
    if command == "Stop":
        break
    command_args = command.split("-")
    action = command_args[0]
    guest = command_args[1]
    meal = command_args[2]
    if action == "Like":
        if guest not in liked_meals:
            liked_meals[guest] = []
        if meal not in liked_meals[guest]:
            liked_meals[guest].append(meal)

    if action == "Dislike":
        if guest not in liked_meals:
            print(f"{guest} is not at the party.")
            continue
        if meal not in liked_meals[guest]:
            print(f"{guest} doesn't have the {meal} in his/her collection.")
        if meal in liked_meals[guest]:
            print(f"{guest} doesn't like the {meal}.")
            dislike_meals[guest] = []
            dislike_meals[guest].append(meal)
            liked_meals[guest].remove(meal)


for guest, meal in liked_meals.items():
    print(f"{guest}: {', '.join(meal)}")

print(f"Unliked meals: {len(dislike_meals)}")