number_cars = int(input())
cars_list = {}

for cars in range(number_cars):
    car_arg = input().split("|")
    car_name = car_arg[0]
    millage = int(car_arg[1])
    fuel = int(car_arg[2])
    cars_list[car_name] = {"mileage": millage, "fuel": fuel}

while True:
    line = input()
    if line == "Stop":
        break
    command_args = line.split(" : ")
    command = command_args[0]

    if command == "Drive":
        car = command_args[1]
        distance = int(command_args[2])
        fuel = int(command_args[3])
        if cars_list[car]["fuel"] < fuel:
            print("Not enough fuel to make that ride")
        else:
            cars_list[car]["mileage"] += distance
            cars_list[car]["fuel"] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if cars_list[car]["mileage"] >= 100000:
            print(f"Time to sell the {car}!")
            del cars_list[car]

    if command == "Refuel":
        car = command_args[1]
        fuel = int(command_args[2])
        if cars_list[car]["fuel"] + fuel > 75:
            needed_fuel = 75 - cars_list[car]["fuel"]
            print(f"{car} refueled with {needed_fuel} liters")
            cars_list[car]["fuel"] += needed_fuel
        else:
            print(f"{car} refueled with {fuel} liters")
            cars_list[car]["fuel"] += fuel

    if command == "Revert":
        car = command_args[1]
        amount_reverted = int(command_args[2])
        if cars_list[car]["mileage"] - amount_reverted < 10000:
            cars_list[car]["mileage"] = 10000
        else:
            print(f"{car} mileage decreased by {amount_reverted} kilometers")
            cars_list[car]["mileage"] -= amount_reverted

for car in cars_list:
    print(f"{car} -> Mileage: {cars_list[car]['mileage']} kms, Fuel in the tank: {cars_list[car]['fuel']} lt.")