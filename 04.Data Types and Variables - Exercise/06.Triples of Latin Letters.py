import string
letters = string.ascii_lowercase
n = int(input())
combinations = [f"{letters[i]}{letters[j]}{letters[k]}"
                for i in range(n)
                for j in range(n)
                for k in range(n)
                ]
print(*combinations, sep="\n")