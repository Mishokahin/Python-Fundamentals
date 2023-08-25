divisor = int(input())
boundary = int(input())
number = [i for i in range(boundary+1) if i % divisor == 0 and boundary >= i > 0]
print(max(number))