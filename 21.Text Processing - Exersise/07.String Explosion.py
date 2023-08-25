characters_to_explode = input()

strength = 0

new_string = ""

for idx in range(len(characters_to_explode)):
    if strength > 0 and characters_to_explode[idx] != ">":
        strength -= 1
    elif characters_to_explode[idx] == ">":
        strength += int(characters_to_explode[idx + 1])
        new_string += characters_to_explode[idx]
    else:
        new_string += characters_to_explode[idx]

print(new_string)
