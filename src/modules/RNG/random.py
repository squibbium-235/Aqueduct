import random

def randomNumber():
    print("Random Number Generators\n")
    print("(1)      Random Integer")
    print("(2)      Random Decimal")
    print("(3)      Coin Flip")
    print("(4)      Random Percentage")
    print("(5)      Back")
    print("")
    choice = int(input("> "))

    if choice == 1:
        number1 = int(input("Enter the lower number: "))
        number2 = int(input("Enter the higher number: \n"))
        print(random.randint(number1,number2))
        print("")
    elif choice == 2:
        number1 = float(input("Enter the lower decimal number: "))
        number2 = float(input("Enter the higher decimal number: \n"))
        print(random.uniform(number1,number2))
        print("")
    elif choice == 3:
        number1=random.randint(0,1)
        if number1==0:  
            print("Heads!\n")
        elif number1==1:
            print("Tails!\n")
        else:
            print("something has gone horribly fucking wrong...\n")
    elif choice == 4:
        print(str(random.randint(0,100))+"%")
    elif choice == 5:
        return choice
    else:
        print("Invalid option!")