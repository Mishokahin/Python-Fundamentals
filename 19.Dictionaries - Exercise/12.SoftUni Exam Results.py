results = {}
submissions = {}

command = input()

while command != "exam finished":
    command_args = command.split("-")
    exam = command_args[1]
    student = command_args[0]

    if exam == "banned":
        del results[student]

    else:
        result = int(command_args[2])
        if student not in results:
            results[student] = result
        if result > results[student]:
            results[student] = int(result)

    if exam not in submissions:
        submissions[exam] = []
        submissions[exam].append(student)
    else:
        submissions[exam].append(student)

    command = input()

print("Results:")
for student in results:
    print(f"{student} | {results[student]}")
print("Submissions:")
for language in submissions:
    if language != "banned":
        print(f"{language} - {len(submissions[language])}")