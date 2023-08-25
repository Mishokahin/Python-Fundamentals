numbers = [int(i) for i in input().split()]
n = int(input())
[numbers.remove(min(numbers)) for i in range(n)]

print(*numbers, sep=", ")