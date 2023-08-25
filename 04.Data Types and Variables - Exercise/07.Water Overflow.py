pour_count = int(input())
water_in_tank = 0
for i in range(pour_count):
    liters_of_water = int(input())
    if liters_of_water > 255 - water_in_tank:
        print("Insufficient capacity!")
        continue
    else:
        water_in_tank += liters_of_water

print(water_in_tank)