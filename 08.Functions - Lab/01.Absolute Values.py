def absolute(numbers):
    absolute_numbers = [abs(float(i)) for i in numbers.split()]
    return absolute_numbers


print(absolute(input()))