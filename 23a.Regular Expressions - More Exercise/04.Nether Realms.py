import re

demons = [demon.strip() for demon in input().split(",")]
demon_data = {}

for demon in demons:
    name_pattern = r"[^\d\+\-\*\/\.\s]"
    found_name = re.findall(name_pattern, demon)
    health = sum([ord(char) for char in found_name])
    damage_pattern = r"(-?\d+(\.?\d*)?)"
    found_damage = re.findall(damage_pattern, demon)
    damage = sum([float(dmg[0]) for dmg in found_damage])
    modifier_pattern = r"[*+\/+]"
    found_modifier = re.findall(modifier_pattern, demon)
    if damage:
        for modifier in found_modifier:
            if modifier == "*":
                damage *= 2
            else:
                damage /= 2

    demon_data[demon] = health, damage

sorted_demons = [key for key in sorted(demon_data.keys())]
for demon in sorted_demons:
    print(f"{demon} - {demon_data[demon][0]} health, {demon_data[demon][1]:.2f} damage")