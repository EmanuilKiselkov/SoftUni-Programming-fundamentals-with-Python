year = int(input())

next_happy_year = False

while not next_happy_year:
    year += 1
    set_year = set()
    for loop in range(len(str(year))):
        set_year.add(str(year)[loop])
    next_happy_year = len(str(year)) == len(set_year)
print(year)