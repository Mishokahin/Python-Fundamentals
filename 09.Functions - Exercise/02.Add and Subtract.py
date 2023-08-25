def add_and_subtract(a, b, c):

    def sum_numbers():
        return a + b

    def subtract():
        return sum_numbers() - c

    return subtract()


print(add_and_subtract(int(input()), int(input()), int(input())))