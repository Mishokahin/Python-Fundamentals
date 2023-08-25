usernames = input().split(", ")
valid_usernames = []

for username in usernames:
    if 3 <= len(username) <= 16:
        valid_characters = []
        for character in username:
            if character.isdigit() or character.isalpha() or character == "-" or character == "_":
                valid_characters.append(True)
            else:
                valid_characters.append(False)

        if all(valid_characters):
            valid_usernames.append(username)

for user in valid_usernames:
    print(f"{user}")