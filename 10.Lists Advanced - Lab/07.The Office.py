def the_office(employees_happiness, factor):
    happiness_refactored = list((int(i)*factor) for i in employees_happiness)
    average_happiness = sum(happiness_refactored)/len(happiness_refactored)
    happy_count = len(list(i for i in happiness_refactored if i >= average_happiness))
    total_count = len(employees_happiness)
    if happy_count >= total_count * 0.5:
        return f"Score: {happy_count}/{total_count}. Employees are happy!"
    else:
        return f"Score: {happy_count}/{total_count}. Employees are not happy!"


print(the_office(input().split(), int(input())))