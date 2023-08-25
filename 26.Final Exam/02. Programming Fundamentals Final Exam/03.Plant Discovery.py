number_of_plant = int(input())

discovered_plants = {}

for plant in range(number_of_plant):
    plant_data = input().split("<->")
    name = plant_data[0]
    rarity = plant_data[1]
    discovered_plants[name] = {"Rarity": rarity, "Rating": []}

while True:
    line = input()
    if line == "Exhibition":
        break

    action, plant_to = line.split(": ")

    if action == "Rate":
        plant_name, rating = plant_to.split(" - ")
        if plant_name in discovered_plants:
            discovered_plants[plant_name]["Rating"] += [float(rating)]
        else:
            print("error")

    if action == "Update":
        plant_name, new_rarity = plant_to.split(" - ")
        if plant_name in discovered_plants:
            discovered_plants[plant_name]["Rarity"] = new_rarity
        else:
            print("error")

    if action == "Reset":
        plant_name = plant_to
        if plant_name in discovered_plants:
            discovered_plants[plant_name]["Rating"] = []
        else:
            print("error")

print("Plants for the exhibition:")
for exhibit, values in discovered_plants.items():
    average_rating = 0
    if values["Rating"]:
        average_rating = sum(values["Rating"]) / len(values["Rating"])
    print(f"- {exhibit}; Rarity: {values['Rarity']}; Rating: {average_rating:.2f}")