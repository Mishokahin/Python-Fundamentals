def perfect_number(n):
    result = sum([i for i in range(1, n) if n % i == 0])
    if result == n:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


print(perfect_number(int(input())))