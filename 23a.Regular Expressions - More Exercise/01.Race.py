import re

racers = {name: 0 for name in input().split(", ")}

while True:
    racer = input()
    if racer == "end of race":
        break

    name_regex = r"[A-Za-z]"
    racer_name = "".join([char for char in re.findall(name_regex, racer)])

    if racer_name in racers:
        score_regex = r"\d"
        racer_score = sum([int(km) for km in re.findall(score_regex, racer)])
        racers[racer_name] += racer_score

sorted_racers = dict(sorted(racers.items(), key=lambda x: x[1], reverse=True))
first_racer = list(sorted_racers.keys())[0]
second_racer = list(sorted_racers.keys())[1]
third_racer = list(sorted_racers.keys())[2]

print(f"1st place: {first_racer}")
print(f"2nd place: {second_racer}")
print(f"3rd place: {third_racer}")