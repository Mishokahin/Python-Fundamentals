length = int(input())
counter = 0
string = [input() for i in range(length)]
for i in string:
    if i == "(":
        counter += 1
    if i == ")":
        counter -= 1
    if 0 != counter != 1:
        print("UNBALANCED")
        exit()

print("BALANCED")
