def min_max_sum(string):
    numbers = [int(i) for i in string.split()]
    return f"The minimum number is {min(numbers)}" \
           f"\nThe maximum number is {max(numbers)}" \
           f"\nThe sum number is: {sum(numbers)}"


print(min_max_sum(input()))