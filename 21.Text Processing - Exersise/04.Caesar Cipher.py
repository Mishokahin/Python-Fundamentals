phrase = input()
encrypted_message = "".join(chr(ord(character) + 3) for character in phrase)

print(encrypted_message)

