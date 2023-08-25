event_list = input().split("|")
energy = 100
coins = 100
events = [str(i).split("-") for i in event_list]
for i in range(len(events)):
    event = events[i][0]
    if event == "rest":
        if energy + int(events[i][1]) > 100:
            print(f"You gained {abs(100 - energy)} energy.")
            energy = 100
        else:
            energy += int(events[i][1])
            print(f"You gained {int(events[i][1])} energy.")
        print(f"Current energy: {energy}.")
    elif event == "order":
        if energy >= 30:
            earned = int(events[i][1])
            coins += earned
            print(f"You earned {earned} coins.")
            energy -= 30
        else:
            print("You had to rest!")
            energy += 50
    else:
        ingredient = event
        if int(events[i][1]) <= coins:
            print(f"You bought {ingredient}.")
            coins -= int(events[i][1])
        else:
            print(f"Closed! Cannot afford {ingredient}.")
            exit()

print("Day completed!")
print(f"Coins: {coins}")
print(f"Energy: {energy}")