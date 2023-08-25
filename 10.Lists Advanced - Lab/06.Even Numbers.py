numbers = input().split(", ")

print(list(i for i in range(len(numbers)) if int(numbers[i]) % 2 == 0))