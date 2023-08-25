words = input().split()
result = ""

for word in words:
    length = len(word)
    result += word * length

print(result)