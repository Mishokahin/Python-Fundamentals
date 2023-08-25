size_of_a_side = float(input())
total_area = size_of_a_side * size_of_a_side * 6
total_covered_area = 0
number_of_sheets = int(input())

for sheet in range(number_of_sheets):
    sheet_length = float(input())
    sheet_width = float(input())
    covered_area = sheet_length * sheet_width
    if (sheet + 1) % 3 == 0:
        covered_area = covered_area * (1 - 0.25)
    if (sheet + 1) % 5 == 0:
        covered_area = 0
    total_covered_area += covered_area


if total_covered_area >= total_area:
    print("You've covered the gift box!")
    if total_area == 0:
        paper_left = 100
    else:
        paper_left = ((total_covered_area - total_area) / total_covered_area) * 100
    print(f"{paper_left:.2f}% wrap paper left.")

else:
    percentage_covered = (total_covered_area / total_area) * 100
    print("You are out of paper!")
    print(f"{100 - percentage_covered:.2f}% of the box is not covered.")