import re

text = input() + " "
pattern = r'\s_([a-zA-Z0-9]+)\s'

matches = re.findall(pattern, text)

print(",".join(matches))