path_to_file = input().split("\\")
path_to_file_ext = path_to_file[-1]

file_name_args = path_to_file_ext.split(".")
extension = file_name_args.pop()
file_name = ".".join(file_name_args)
print(f"File name: {file_name}")
print(f"File extension: {extension}")