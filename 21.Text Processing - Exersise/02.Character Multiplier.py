string1, string2 = input().split()
string1_characters = [ord(character) for character in string1]
string2_characters = [ord(character) for character in string2]

min_len = min(len(string1_characters), len(string2_characters))
result = 0

for idx in range(min_len):
    result += string1_characters[idx] * string2_characters[idx]

result += sum(character for character in string1_characters[min_len:])
result += sum(character for character in string2_characters[min_len:])

print(result)