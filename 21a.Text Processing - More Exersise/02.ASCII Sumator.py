first_value = ord(input())
second_value = ord(input())
sequence = input()

result = sum([ord(character) for character in sequence if first_value < ord(character) < second_value])

print(result)