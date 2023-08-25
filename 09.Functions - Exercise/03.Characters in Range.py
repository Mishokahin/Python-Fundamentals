def characters_in_range(a, b):
    characters = [chr(i) for i in range(ord(a)+1, ord(b))]
    return characters


print(*characters_in_range(input(), input()))