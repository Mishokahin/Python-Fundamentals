import math
numbers = list(int(i) for i in input().split(", "))
n = max(numbers)
print("\n".join(f"Group of {i*10}'s: {list(num for num in numbers if (i-1) * 10 < int(num) <= i * 10)}"
                for i in range(1, math.ceil(n/10)+1)))