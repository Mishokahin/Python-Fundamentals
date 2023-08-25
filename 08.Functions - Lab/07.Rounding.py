def rounded(string):
    rounded_numbers = [round(float(i)) for i in string.split()]
    return rounded_numbers


print(rounded(input()))