cycle = int(input())

for i in range(cycle):
    command = int(input())
    if command == 88:
        print("Hello")
    elif command == 86:
        print("How are you?")
    elif command == 87 or command <= 85:
        print("GREAT!")
    elif command > 88:
        print("Bye.")




