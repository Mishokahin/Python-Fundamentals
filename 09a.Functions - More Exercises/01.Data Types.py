def data_types(command, string):
    if command == "int":
        return int(string) * 2
    if command == "real":
        return f"{float(string) * 1.5:.2f}"
    if command == "string":
        return f"${string}$"


print(data_types(input(), input()))