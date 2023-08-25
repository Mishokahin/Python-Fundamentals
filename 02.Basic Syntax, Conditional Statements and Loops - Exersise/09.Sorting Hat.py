import sys
schools = {range(1, 5): "Gryffindor",
           range(5, 6): "Slytherin",
           range(6, 7): "Ravenclaw",
           range(7, sys.maxsize): "Hufflepuff"
           }
name = input()

while name != "Welcome!":
    if name == "Voldemort":
        print("You must not speak of that name!")
        exit()
    else:
        school = [schools[key] for key in schools if len(name) in key]
        print(f"{name} goes to {str(*school)}.")

    name = input()

print("Welcome to Hogwarts.")