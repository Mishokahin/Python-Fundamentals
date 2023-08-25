registered = {}

users = int(input())

for user in range(users):
    data = input().split()
    command = data[0]
    username = data[1]
    if command == "register":
        license_plate_number = data[2]
        if username in registered:
            print(f"ERROR: already registered with plate number {registered[username]}")
        else:
            registered[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")
    else:
        if username not in registered:
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            registered.pop(username)

for username, license_plate_number in registered.items():
    print(f"{username} => {license_plate_number}")