import random

def randomFloat():
    number1 = float(input("Enter the lower decimal number: "))
    number2 = float(input("Enter the higher decimal number: \n"))
    print(random.uniform(number1,number2))
    print("")