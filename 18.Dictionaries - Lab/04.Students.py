students = {}
command = input()

while ":" in command:
    name, ID, course = command.split(":")
    if course not in students:
        students[course] = {}
    students[course][ID] = name
    command = input()

requested_course = " ".join(command.split("_"))
for key, value in students.items():
    if key == requested_course:
        for ID, name in value.items():
            print(f"{name} - {ID}")