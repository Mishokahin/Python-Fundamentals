countries, capitals = input().split(", "), input().split(", ")

for country, capital in zip(countries, capitals):
    print(f"{country} -> {capital}")