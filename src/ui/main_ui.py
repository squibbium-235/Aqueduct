# i have an incredibly homosexual friend. and i have put you in here to be forever rememberd for touching me every day

import random

while True:
    print("Main Menu\n")
    print("(1)      Random Number Generation")
    print("(2)      Converters")
    print("(3)      Quit")
    choice = input("> ")

    if choice == '1':
        while True:
            print("Random Number Generators\n")
            print("(1)      Random Integer")
            print("(2)      Random Decimal")
            print("(3)      Coin Flip")
            print("(4)      Random Percentage")
            print("(5)      Back")
            choice = input("> ")

            if choice == '1':
                number1 = int(input("Enter the lower number: "))
                number2 = int(input("Enter the higher number: \n"))
                print(random.randint(number1,number2))
                print("")
            elif choice == '2':
                number1 = float(input("Enter the lower decimal number: "))
                number2 = float(input("Enter the higher decimal number: \n"))
                print(random.uniform(number1,number2))
                print("")
            elif choice == '3':
                number1=random.randint(0,1)
                if number1==0:
                    print("Heads!\n")
                elif number1==1:
                    print("Tails!\n")
                else:
                    print("something has gone horribly fucking wrong...\n")
            elif choice == '4':
                print(str(random.randint(0,100))+"%")
            elif choice == '5':
                break  # Go back to the main menu
            else:
                print("Invalid choice. Please try again.")

    elif choice == '2':
        while True:
            print("(1)      Distance")
            print("(2)      Mass")
            print("(3)      Temperature")
            print("(4)      Volume")
            print("(5)      Time")
            print("(6)      Area")
            print("(7)      Back")
    elif choice == '3':
        break  # Quit the program
    else:
        print("Invalid choice. Please try again.")