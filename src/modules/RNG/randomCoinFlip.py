import random

def randomCoinFlip():
    number1=random.randint(0,1)
    if number1==0:
        print("Heads!\n")
    elif number1==1:
        print("Tails!\n")
    else:
        print("something has gone horribly fucking wrong...\n")