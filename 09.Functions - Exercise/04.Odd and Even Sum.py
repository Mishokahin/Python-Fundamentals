def odd_and_even_sum(sting):
    sum_of_even_digits = sum([int(i) for i in sting if int(i) % 2 == 0])
    sum_of_odd_digits = sum([int(i) for i in sting if int(i) % 2 != 0])
    return f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"


print(odd_and_even_sum(input()))