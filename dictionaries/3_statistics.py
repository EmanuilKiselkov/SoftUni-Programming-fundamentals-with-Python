product = {}

command = input()
while command != "statistics":
    key, value = command.split(": ")
    if key not in product:
        product[key] = 0
        product[key]+= int(value)
    else:
        product[key]+= int(value)
    command = input()


print(f"Products in stock:")
for keys, values in product.items():
    print(f"- {keys}: {values}")
print(f"Total Products: {len(product.values())}")
print(f"Total Quantity: {sum(product.values())}")
