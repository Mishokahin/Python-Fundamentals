import re

pattern = r"\b(?P<day>\d{2})([-.\/])(?P<month>[A-Z][a-z]{2})(\2)(?P<year>\d{4})\b"

dates = input()

valid_dates = re.findall(pattern, dates)

for date in valid_dates:
    day, month, year = date[0], date[2], date[4]
    print(f"Day: {day}, Month: {month}, Year: {year}")