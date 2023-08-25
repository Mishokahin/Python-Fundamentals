def calculation(operation, a, b):
    result = None
    if operation == "multiply":
        result = a * b
    elif operation == "divide":
        result = int(a / b)
    elif operation == "add":
        result = a + b
    elif operation == "subtract":
        result = a - b
    return result


print(calculation(input(), int(input()), int(input())))