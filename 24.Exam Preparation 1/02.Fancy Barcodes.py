import re

number_of_items = int(input())

for i in range(number_of_items):
    item = input()
    patter = r"@#+([A-Z][a-zA-Z0-9]{4,}[A-Z])@#+"

    match = re.search(patter, item)

    if match:
        product_group = re.findall(r"(\d+)", match.group(1))
        if product_group:
            print(f"Product group: {''.join(product_group)}")
        else:
            print(f"Product group: 00")
    else:
        print("Invalid barcode")
