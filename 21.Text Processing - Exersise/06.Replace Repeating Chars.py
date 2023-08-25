letters = input()

new_string = letters[0]

for letter in letters:
    if letter == new_string[-1]:
        continue
    new_string += letter

print(new_string)
