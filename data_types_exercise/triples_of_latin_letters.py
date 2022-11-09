number_of_symbols = int(input())

for first_symbols in range(number_of_symbols):
    for second_symbols in range(number_of_symbols):
        for third_symbols in range(number_of_symbols):
            print(f"{chr(97 + first_symbols)}{chr(97 + second_symbols)}{chr(97 + third_symbols)}")