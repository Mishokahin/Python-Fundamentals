courses = {}

command = input()

while command != "end":
    course_name, student_name = command.split(" : ")

    if course_name not in courses:
        courses[course_name] = []
    courses[course_name].append(student_name)
    command = input()

for course in courses:
    print(f"{course}: {len(courses[course])}")
    for student in courses[course]:
        print(f"-- {student}")