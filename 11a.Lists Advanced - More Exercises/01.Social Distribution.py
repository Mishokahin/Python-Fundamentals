population = list(int(i) for i in input().split(", "))
minimum_wealth = int(input())


for index, person in enumerate(population):

    if person < minimum_wealth:
        population[index] += minimum_wealth - person

new_wealth = list(bool(int(i) >= minimum_wealth) for i in population)

if all(new_wealth):
    print(population)
else:
    print("No equal distribution possible")