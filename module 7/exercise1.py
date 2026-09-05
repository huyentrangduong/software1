import random

def roll_dice():
    for i in range(2):
        number = random.randint(1, 6)
        print(number)


roll_dice()