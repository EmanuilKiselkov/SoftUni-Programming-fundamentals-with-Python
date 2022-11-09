input_number = input().split(" ")
opposite_number = []

for element in input_number:
    current_number = -int(element)
    opposite_number.append(current_number)
print(opposite_number)