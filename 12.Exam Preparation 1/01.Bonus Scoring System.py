import math
student_count = int(input())
lectures_count = int(input())
additional_bonus = int(input())

maximum_bonus = 0
maximum_attendance = 0

for student in range(student_count):
    attendance = int(input())
    current_bonus = (attendance / lectures_count) * (5 + additional_bonus)
    if attendance > maximum_attendance:
        maximum_attendance = attendance
    if current_bonus > maximum_bonus:
        maximum_bonus = current_bonus

print(f"Max Bonus: {math.ceil(maximum_bonus)}.")
print(f"The student has attended {maximum_attendance} lectures.")