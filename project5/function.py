from item import Item

def main_menu():
    choice = input("\n✅ Enter a command from the main menu:\n 1.explore\n 2.run\n 3.take\n 4.harvest\n 5.lopeta\n")
    return choice


def score (total):
    total = total + 10
    return total

def inventory (items):
    for item in items:
        print(f"   - {item.name} and {item.weight}g")

def explore(bag):
    new_item = input("What item would you like to pick up and add to your bag? ")
    new_weight = int(input("What is the weight of the item? "))
    print("\nCheck the items in your bag:")
    item_one = Item(new_item, new_weight)
    bag.append(item_one)
    inventory(bag)

def run(bag):
    item_run = Item("Water Bottle",100)
    for item_run in bag:
        bag.remove(item_run)
        inventory (bag)


def take(bag):
    item = input("What item do you want to collect? ")
    weight = int(input("What is the weight of the item? "))
    item_two = Item(item, weight)
    bag.append(item_two)
    print("Check the items in your bag:") 
    inventory (bag)

def harvest(bag):
    item_three = Item("Crops 🌾", 300)
    bag.append(item_three)
    inventory (bag)

   


