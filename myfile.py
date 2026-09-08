
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


#while
round = 3
while round >= 0:
    print("Hi")
    rounds = rounds -1

#update
# 1. INPUT
#user_input = input(...)

# 2. INITIALIZE
#smallest = None
#largest = None

# 3. CONDITION
#while user_input != "":

    # 4. CONVERT
    #number = int(user_input)

    # 5. PROCESS / COMPARE
    #if ...:
    #    ...

    #if ...:
    #   ...

    # 6. UPDATE / GET NEXT INPUT
    #user_input = input(...)

# 7. RESULT
#print(...)

number = int(input("Enter a number: "))
numbers = []

while number != "":
    numbers.append(number)
    number = int(input("Enter a number: "))
    
numbers.sort()    
print (numbers)