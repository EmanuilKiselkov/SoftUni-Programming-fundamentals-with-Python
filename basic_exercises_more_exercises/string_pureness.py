number_strings = int(input())

for cycles in range(number_strings):
    command = input()
    if "," in command \
           or "." in command \
            or "_" in command:
        print(f"{command} is not pure!")
    else:
        print(f"{command} is pure.")