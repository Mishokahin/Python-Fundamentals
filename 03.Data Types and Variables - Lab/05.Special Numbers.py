n = input()

for num in range(1, int(n) + 1):
    sum_of_digits = 0
    if num >= 10:
        digits = str(num)
        sum_of_digits = sum([int(digits[i]) for i in range(len(digits))])
    else:
        sum_of_digits = num

    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
        print(f"{num} -> True")
    else:
        print(f"{num} -> False")