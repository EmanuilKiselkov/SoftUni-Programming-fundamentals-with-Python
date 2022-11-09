items = input().split(" ")
bakery = {}

for element in range(0, len(items), 2):
    key = items[element]
    value = items[element + 1]
    bakery[key] = int(value)

searched_product = input().split(" ")

for product in searched_product:
    if product in bakery:
        print(f"We have {bakery[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")