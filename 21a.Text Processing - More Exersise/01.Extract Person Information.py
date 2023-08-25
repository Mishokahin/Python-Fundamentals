count = int(input())

for person in range(count):
    text = input()
    name = text[text.index("@")+1:text.index("|")]
    age = text[text.index("#")+1:text.index("*")]
    print(f"{name} is {age} years old.")