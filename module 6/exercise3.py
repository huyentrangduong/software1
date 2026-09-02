#Write a program that asks the user for an integer and tells if the number is a prime number. 
#Prime numbers are number that are only divisible by one or the number itself. 
#For example, 13 is a prime number as it can only be divided by 1 or 13 so that the result is an integer. 
#On the other hand, 21 is not a prime number as it is divisible by 3 and 7. Requirements:
#The program should ask the user for an integer
#The program should tell if the number is a prime number or not

number = int(input ("Enter an integer: "))
x = 2

if number < 2:
    print (number,"is not a prime number")


while number >= x: 
    if number % x == 0:
        print (number,"is not a prime number")
    break

number = int(input ("Enter an integer: "))
number += 1

#print (number,"is a prime number")

