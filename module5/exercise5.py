#Write a program that asks the user for a username and password. 
#If either or both are incorrect, the program asks the user to enter the username and password again. 
#This continues until the login information is correct or wrong credentials have been entered five times. 
#If the information is correct, the program prints out "Welcome". 
#After five failed attempts the program prints out "Access denied". 
#The correct username is python and password rules.


username = "python"
password = "rules"
attempts = 0

while attempts < 5:
    username_input = input("Enter username: ")
    password_input = input("Enter password: ")

    attempts += 1

    if username_input == username and password_input == password:
        print("Welcome")
        break

    elif attempts < 5:
        print("Incorrect username or password. Please try again.")

    else:
        print("Access denied")