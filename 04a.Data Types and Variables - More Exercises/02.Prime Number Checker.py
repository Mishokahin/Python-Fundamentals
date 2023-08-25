number = int(input())

if number < 2:
    print("False")
else:
    number_checker = [i for i in range(2, number+1) if number % i == 0]
    if len(number_checker) == 1:
        print("True")
    else:
        print("False")