needed_materials = {"shards": 0,
                    "fragments": 0,
                    "motes": 0
                    }

junk = {}
legendary_item = {"shards": "Shadowmourne",
                  "fragments": "Valanyr",
                  "motes": "Dragonwrath"
                  }

crafted = False
while not crafted:
    command = input()
    resources = command.split()

    for idx in range(0, len(resources)-1, 2):
        quantity = int(resources[idx])
        material = resources[idx + 1].lower()
        if material in needed_materials:
            needed_materials[material] += quantity
            if needed_materials[material] >= 250:
                needed_materials[material] -= 250
                crafted = True
                print(f"{legendary_item[material]} obtained!")
                break
        else:
            if material in junk:
                junk[material] += quantity
            else:
                junk[material] = quantity

for material, quantity in needed_materials.items():
    print(f"{material}: {quantity}")

for material, quantity in junk.items():
    print(f"{material}: {quantity}")