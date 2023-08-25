import re

pattern = r"\+359-2-[0-9]{3}-[0-9]{4}|\+359 2 [0-9]{3} [0-9]{4}\b"
phone_book = input()
valid_phone_numbers = re.findall(pattern, phone_book)
print(", ".join(valid_phone_numbers))