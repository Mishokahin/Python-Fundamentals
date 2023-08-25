initial_list = input().split(", ")
numbers, zeros = [int(i) for i in initial_list if int(i) != 0], [int(i) for i in initial_list if int(i) == 0]
print(numbers + zeros)