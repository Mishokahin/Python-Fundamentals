number_of_songs = int(input())
song_collection = {}

for song in range(number_of_songs):
    song_data = input().split("|")
    piece = song_data[0]
    composer = song_data[1]
    key = song_data[2]
    song_collection[piece] = {"composer": composer, "key": key}

while True:
    line = input()
    if line == "Stop":
        break
    command_args = line.split("|")

    command = command_args[0]

    if command == "Add":
        piece = command_args[1]
        if piece in song_collection:
            print(f"{piece} is already in the collection!")
        else:
            composer = command_args[2]
            key = command_args[3]
            print(f"{piece} by {composer} in {key} added to the collection!")
            song_collection[piece] = {"composer": composer, "key": key}

    if command == "Remove":
        piece = command_args[1]
        if piece not in song_collection:
            print(f"Invalid operation! {piece} does not exist in the collection.")
        else:
            print(f"Successfully removed {piece}!")
            del song_collection[piece]

    if command == "ChangeKey":
        piece = command_args[1]
        if piece not in song_collection:
            print(f"Invalid operation! {piece} does not exist in the collection.")
        else:
            new_key = command_args[2]
            print(f"Changed the key of {piece} to {new_key}!")
            song_collection[piece]["key"] = new_key

for piece in song_collection:
    print(f"{piece} -> Composer: {song_collection[piece]['composer']}, Key: {song_collection[piece]['key']}")