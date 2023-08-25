import re
keys = [int(key) for key in input().split()]

while True:
    encrypted_message = input()
    if encrypted_message == "find":
        break

    decrypded_message = ""
    count = 0
    for character in encrypted_message:
        if count == len(keys):
            count = 0
        decrypded_message += chr(ord(character)-keys[count])
        count += 1

    treasure_type_indexes = [int(idx) for idx in range(len(decrypded_message)) if decrypded_message[idx] == "&"]
    type_of_treasure = decrypded_message[treasure_type_indexes[0]+1:treasure_type_indexes[1]]
    treasure_coordinates = decrypded_message[decrypded_message.index("<")+1:decrypded_message.index(">")]

    print(f"Found {type_of_treasure} at {treasure_coordinates}")