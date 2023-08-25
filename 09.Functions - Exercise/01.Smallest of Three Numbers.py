def smallest(a, b, c):
    numbers = [a, b, c]
    numbers.sort()
    return numbers[0]


print(smallest(int(input()), int(input()), int(input())))