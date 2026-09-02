#Write a program that asks the user how many dice to roll. The program rolls all the dice once and prints out the sum of the numbers. 
#Use a for loop. The program should ask the user for input with the following text: How many dice to roll:
#The program should print exactly the following text (example if the user inputs the number 5): Sum of the dice: 15

import random
rolls = int(input("How many dice to roll: "))

sum = 0

for roll in range(rolls):
    sum = sum + random.randint(1,9)
    print(f"Sum of the dice: {sum}")
