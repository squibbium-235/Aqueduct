import random

def randomInt():
    number1 = int(input("Enter the lower number: "))
    number2 = int(input("Enter the higher number: \n"))
    print(random.randint(number1,number2))
    print("") 