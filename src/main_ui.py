# i have an incredibly homosexual friend. and i have put you in here to be forever rememberd for touching me every day

import random
from modules.RNG.random import randomNumber
while True:
    print("Main Menu\n")
    print("(1)      Random Number Generation")
    print("(2)      Converters")
    print("(3)      Quit")
    choice = input("> ")

    if choice == '1':
        while True:
            randomNumber()
            if choice == 5:
                break
    elif choice == '2':
        while True:
            print("(1)      Distance")
            print("(2)      Mass")
            print("(3)      Temperature")
            print("(4)      Volume")
            print("(5)      Time")
            print("(6)      Area")
            print("")
            print("(7)      Back")
            choice = int(input("> "))
            if choice == 1:
                print("(1)      Metric to Metric")
                print("(2)      Metric to Imperial")
                print("(3)      Imperial to Imperial")
                print("(4)      Imperial to Metric")
                print("")
                print("(5)      Back")
                choice = int(input("> "))
                if choice == 1:
                    

    elif choice == '3':
        break  # Quit the program
    else:
        print("Invalid choice. Please try again.")