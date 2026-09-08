def change():
    city = "Vantaa"
    print("At the end of the function: " + city)
    return

city = "Helsinki"
print("At the beginning in the main program: " + city)
change()
print("At the end of the main program: " + city)


def inventory(items):
    print("You have the following items:")
    for item in items:
        print("- " + item)
    return

backpack = ["Water bottle", "Map", "Compass"]
inventory(backpack)
backpack.append("Swiss Army knife")
inventory(backpack)


def add(x, y):
    result = x + y
    return result

answer = add(5, 3)

print(answer)