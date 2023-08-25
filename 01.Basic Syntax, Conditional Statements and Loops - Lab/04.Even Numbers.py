numbers = int(input())
for num in range(numbers):
    number = int(input())
    if number % 2 != 0:
        print(f"{number} is odd!")
        exit()

print("All numbers are even.")