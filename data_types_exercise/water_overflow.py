water_tank = 255
lines = int(input())
tank_capacity = 0

for number_lines in range(lines):
    add_liquid = int(input())
    tank_capacity += add_liquid
    if tank_capacity > water_tank:
        print("Insufficient capacity!")
        tank_capacity -= add_liquid
        continue

print(tank_capacity)
