
import random
sided_roll = int(input("the number of sides: "))

def roll_dice(sided_roll):
    number = random.randint(1, sided_roll)
    side = int(input("the number of sides: "))
    return number

number = 0

while number != sided_roll:
    number = roll_dice(sided_roll)
    print(number)
