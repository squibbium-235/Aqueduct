import random

quit=0
isHome=1
while quit != 1:
    if isHome:
        print("Aqueduct")
        print("")
        print("Pick an option below: ")
        print("(1)      Random Number Generation")
        print("(2)      Converters")
        print("(3)      Quit")
        command = input("> ")
        if command == 1:
            isHome=0
            print("Random Number Generators")
            print("")
            print("(1)      Random Integer")
            print("(2)      Random Decimal")
            print("(3)      Coin Flip")
            print("(4)      Random Percentage")
            print("(5)      Back")
            command = input("> ")
            if command == 1:
                number1 = int(input("Enter the lower integer to start at: "))
                number2 = int(input("Enter the highest integer to finish at: "))
                print(random.randing(number1,number2))