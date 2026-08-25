
money = float(input("Give money: "))

cost_of_coffee = 5

if money >= cost_of_coffee:
    print ("You have enough for coffee")
    if money >= 20:
        print ("  You can also buy cake")
    takeout = input("Coffee to go?")
    if takeout == "yes":
        print("User is taking the coffee to go")
    if takeout == "no":
        print("User is having the coffee in the cafe")


age = int(input("Enter age: "))
if 15 <= age < 18:
    weight = float(input("Enter weight (kg): "))
if (age >= 18 or age >= 15 and weight >= 55):
    print("The medicine can be used.")