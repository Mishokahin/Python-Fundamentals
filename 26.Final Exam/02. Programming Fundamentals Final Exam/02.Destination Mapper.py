import re

text = input()

pattern = r"(=|\/)([A-Z][a-zA-Z]{2,})\1"

destinations = [match[1] for match in re.findall(pattern, text)]
travel_points = sum([len(destination) for destination in destinations])

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {travel_points}")