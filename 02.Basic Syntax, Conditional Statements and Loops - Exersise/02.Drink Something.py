import sys
drinks = {range(-sys.maxsize, 15): "toddy",
          range(15, 19): "coke",
          range(19, 22): "beer",
          range(22, sys.maxsize): "whisky"
          }
age = int(input())
drink = [drinks[key] for key in drinks if age in key]
print(f"drink {str(*drink)}")