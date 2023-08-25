cell_list = input().split("#")
total_water = int(input())
effort = 0
total_fire = 0
cleared_cells = []
fire_levels = {"High": range(81, 126), "Medium": range(51, 81), "Low": range(1, 51)}
cells = [str(i).split(" = ") for i in cell_list]

for i in range(len(cells)):
    if cells[i][0] in fire_levels and int(cells[i][1]) in fire_levels[cells[i][0]]:
        if int(cells[i][1]) <= total_water:
            total_water -= int(cells[i][1])
            total_fire += int(cells[i][1])
            effort += int(cells[i][1]) * 0.25
            cleared_cells.append(int(cells[i][1]))

print(f"Cells:")
for i in cleared_cells:
    print(f"- {i}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")