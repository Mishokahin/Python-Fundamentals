def sorted_list(string):
    numbers = [int(i) for i in string.split()]
    return sorted(numbers)


print(sorted_list(input()))