import re


income = 0

while True:
    text = input()
    if text == "end of shift":
        break

    pattern = r"(\%[A-Z][a-z]+\%)([^\|\$\%\.]*?)(\<\w+\>)([^\|\$\%\.]*?)(\|[0-9]+\|)([^\|\$\%\.]*?)([0-9.]+[0-9])(?=\$)"
    matches = re.search(pattern, text)
    if matches:
        customer = matches.group(1)[1:-1]
        product = matches.group(3)[1:-1]
        count = int(matches.group(5)[1:-1])
        price = float(matches.group(7))
        total = count * price
        income += total
        print(f"{customer}: {product} - {total:.2f}")

print(f"Total income: {income:.2f}")