import re

links = []

while True:
    text = input()
    if not text:
        break

    pattern = r"(www\.[A-Za-z\d\-]+(\.[a-z]+)+)"
    matches = re.findall(pattern, text)
    links.extend(match[0] for match in matches)

for link in links:
    print(link)
