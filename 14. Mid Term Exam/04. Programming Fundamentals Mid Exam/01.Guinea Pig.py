food = float(input()) * 1000
hay = float(input()) * 1000
cover = float(input()) * 1000
weight = float(input()) * 1000

for day in range(1, 31):
    food -= 300
    if day % 2 == 0:
        hay -= food * 0.05
    if day % 3 == 0:
        cover -= weight * 1/3

    if food <= 0 or hay <= 0 or cover <= 0:
        print("Merry must go to the pet store!")
        exit()

excess_food = food/1000
excess_hay = hay/1000
excess_cover = cover/1000

print(f"Everything is fine! Puppy is happy! Food: {excess_food:.2f}, "
      f"Hay: {excess_hay:.2f}, Cover: {excess_cover:.2f}.")