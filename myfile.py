import math

radius = input("Enter the radius of the circle: ")

radius = float(radius)

area = radius **2 * math.pi

print ("Enter the radius of the circle: The area of the circle is " + str(area))

#excercise 3
length = (input("Enter the length of the rectangle: ")
length_int = int(length)

width = (input("Enter the width of the rectangle: ")
width_int = int(width)

perimeter = (length_int + width_int)*2
area = (length_int * width_int)

print("The area of the rectangle is " + area)
print("The perimeter of the rectangle is " + perimeter)