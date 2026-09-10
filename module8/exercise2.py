names = set()

new_name = input ("enter names: ")
while new_name != "":
    if new_name in names:
        print("Existing name")

    else:
        names.add(new_name)
        print("New name")

    new_name = input("Enter name: ")