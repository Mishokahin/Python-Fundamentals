employee = int(input()), int(input()), int(input())
employee_efficiency = sum(employee)
student_count = int(input())

time_needed = 0

while student_count > 0:
    time_needed += 1
    if time_needed % 4 == 0:
        pass
    else:
        student_count -= employee_efficiency


print(f"Time needed: {time_needed}h.")