gallon = 3.785
volume_gallon = float(input("Enter a volume in American gallons (negative value to quit): "))
conversion = float(gallon*volume_gallon)
n = 0

def gallons_to_liters (conversion):
    conversion = float(gallon*volume_gallon)
    return conversion

while volume_gallon >= 0:
    print (f"{volume_gallon:.1f} American gallons is {conversion:.2f} liters.")
    volume_gallon = int(input("Enter a volume in American gallons (negative value to quit): "))
    gallon = 3.785
    conversion = float(gallon*volume_gallon)
n += 1
print("Program finished.")      


            