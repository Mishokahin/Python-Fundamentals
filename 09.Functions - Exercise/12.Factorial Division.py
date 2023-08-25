def factorial_division(a, b):
    result = 1
    for i in range(a, b, -1):
        result *= i
    return result


print(f"{factorial_division(int(input()), int(input())):.2f}")