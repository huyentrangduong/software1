
#Write a program that asks the user to enter numbers until they enter an empty string to quit. 
#Finally,the program prints out the smallest and largest number from the numbers it received.

user_input = input("Enter a number (or press Enter to quit): ")

smallest_number = None
largest_number = None

while user_input != "":
    number = float(user_input)

    if smallest_number is None or number < smallest_number:
        smallest_number = number

    if largest_number is None or number > largest_number:
        largest_number = number

    user_input = input("Enter a number (or press Enter to quit): ")

print("Smallest number:", smallest_number)
print("Largest number:", largest_number)