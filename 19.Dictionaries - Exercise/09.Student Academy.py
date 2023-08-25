students = {}

student_count = int(input())

for student in range(student_count):
    student_name = input()
    student_grade = float(input())

    if student_name not in students:
        students[student_name] = []
    students[student_name].append(student_grade)

for name in students:
    average_grade = sum(students[name]) / len(students[name])
    if average_grade >= 4.50:
        print(f"{name} -> {average_grade:.2f}")