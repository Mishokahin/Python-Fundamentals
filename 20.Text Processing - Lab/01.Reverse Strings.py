words = []

command = input()

while command != "end":
    words.append(command)
    command = input()

for word in words:
    print(f"{word} = {word[::-1]}")