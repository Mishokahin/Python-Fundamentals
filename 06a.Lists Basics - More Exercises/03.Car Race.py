numbers = input().split()
left_car_score = 0
right_car_score = 0
for i in numbers[:len(numbers)//2]:
    if int(i) == 0:
        left_car_score *= 0.8
    else:
        left_car_score += int(i)
numbers.reverse()
for i in numbers[:(len(numbers)//2)]:
    if int(i) == 0:
        right_car_score *= 0.8
    else:
        right_car_score += int(i)

if left_car_score < right_car_score:
    print(f"The winner is left with total time: {left_car_score:.1f}")
else:
    print(f"The winner is right with total time: {right_car_score:.1f}")