numbers = [int(number) for number in input().split()]
average_number = sum(numbers) / len(numbers)
higher_than_average = [int(num) for num in numbers if num > average_number]

higher_than_average.sort()
higher_than_average.reverse()
if len(higher_than_average) == 0:
    print("No")
elif len(higher_than_average) < 5:
    print(*higher_than_average)
else:
    print(*higher_than_average[0:5])