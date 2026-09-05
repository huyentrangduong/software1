
import math

diameter1 = float(input ("Enter the diameter of the first pizza (cm): "))
price1 = float(input("Enter the price of the first pizza (euros): "))
area1 = (math.pi * (((diameter1/2)/100)**2))

diameter2 = float(input ("Enter the diameter of the second pizza (cm): "))
price2 = float(input("Enter the price of the second pizza (euros): "))
area2 = (math.pi * (((diameter2/2)/100)**2))

def calculate_unit_price (diameter1,price1):
    result1 = price1/(math.pi * (((diameter1/2)/100)**2))
    return result1

def calculate_unit_price (diameter2,price2):
    result2 = price2/(math.pi * (((diameter2/2)/100)**2))

    return result2


answer1 = calculate_unit_price (diameter1,price1)
answer2 = calculate_unit_price (diameter2,price2)

print(f"Unit price of the first pizza: {answer1:.2f} euros/m²")
print(f"Unit price of the second pizza: {answer2:.2f} euros/m²")

if answer1 < answer2:
    print("The first pizza provides better value for money.")
else:
    print("The second pizza provides better value for money.")