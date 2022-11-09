number_of_orders = int(input())
final_price = 0

for cycle_of_orders in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    caps_per_day = int(input())
    if price_per_capsule < 0.01 or price_per_capsule > 100:
        continue
    elif days < 1 or days > 31:
        continue
    elif caps_per_day < 1 or caps_per_day > 2000:
        continue
    price = price_per_capsule * days * caps_per_day
    final_price += price
    print(f"The price for the coffee is: ${price:.2f}")
print(f"Total: ${final_price:.2f}")