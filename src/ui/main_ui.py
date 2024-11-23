import random

while True:
    print("Main Menu")
    print("1. Random Number Generation")
    print("2. Converters")
    print("3. Quit")
    choice = input("> ")

    if choice == '1':
        while True:
            print("Random Number Generators")
            print("1. Random Integer")
            print("2. Random Decimal")
            print("3. Coin Flip")
            print("4. Random Percentage")
            print("5. Back")
            choice = input("> ")

            if choice == '1':
                number1 = int(input("Enter the lower number: "))
                number2 = int(input("Enter the higher number: "))
                print(random.randint(number1,number2))
                print("")
            """elif choice == '2':
                # ... (code for random decimal generation)
            elif choice == '3':
                # ... (code for coin flip)
            elif choice == '4':
                # ... (code for random percentage)
            elif choice == '5':
                break  # Go back to the main menu
            else:
                print("Invalid choice. Please try again.")

    elif choice == '2':
        # ... (code for converters)
    elif choice == '3':
        break  # Quit the program
    else:
        print("Invalid choice. Please try again.")"""