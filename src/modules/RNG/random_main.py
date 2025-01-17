import random
from random_int import randomInt
from random_float import randomFloat
from coin_flip import coinFlip

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
        randomInt()
    elif choice == 2:
        randomFloat()
    elif choice == 3:
        coinFlip()
    elif choice == 4:
        print(str(random.randint(0,100))+"%")
    elif choice == 5:
        return choice
    else:
        print("Invalid option!")