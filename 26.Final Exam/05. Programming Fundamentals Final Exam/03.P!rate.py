towns = {}

while True:
    town_data = input()
    if town_data == "Sail":
        break
    town_args = town_data.split("||")
    town = town_args[0]
    population = int(town_args[1])
    gold = int(town_args[2])
    if town in towns:
        towns[town]["population"] += population
        towns[town]["gold"] += gold
    else:
        towns[town] = {"population": population, "gold": gold}

while True:
    line = input()
    if line == "End":
        break
    line_args = line.split("=>")
    command = line_args[0]
    if command == "Plunder":
        town_to_attack = line_args[1]
        people_to_unalive = int(line_args[2])
        gold_to_steal = int(line_args[3])
        towns[town_to_attack]["population"] -= people_to_unalive
        towns[town_to_attack]["gold"] -= gold_to_steal
        print(f"{town_to_attack} plundered! {gold_to_steal} gold stolen, {people_to_unalive} citizens killed.")
        if towns[town_to_attack]["population"] <= 0 or towns[town_to_attack]["gold"] <= 0:
            print(f"{town_to_attack} has been wiped off the map!")
            del towns[town_to_attack]
    if command == "Prosper":
        town_to_develop = line_args[1]
        gold_to_add = int(line_args[2])
        if gold_to_add < 0:
            print("Gold added cannot be a negative number!")
        else:
            towns[town_to_develop]["gold"] += gold_to_add
            print(f"{gold_to_add} gold added to the city treasury. {town_to_develop} now has"
                  f" {towns[town_to_develop]['gold']} gold.")

if len(towns) == 0:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    count = len(towns)
    print(f"Ahoy, Captain! There are {count} wealthy settlements to go to:")
    for town in towns:
        print(f"{town} -> Population: {towns[town]['population']} citizens, Gold: {towns[town]['gold']} kg")