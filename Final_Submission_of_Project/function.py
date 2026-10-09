from item import Item
from player import Player

def main_menu():
    choice = input("\n✅ Enter a command from the main menu:\n 1.explore\n 2.run\n 3.take\n 4.harvest\n 5.lopeta\n")
    return choice


def score (total):
    total = total + 10
    return total

def inventory (items):
    for item in items:
        print(f"   - {item.name} and {item.quanity}")

def explore(player):
    new_item = input("What item would you like to pick up and add to your bag? ")
    new_weight = int(input("What is the quanity of the item? "))
    print("\nCheck the items in your bag:")
    item1= Item(new_item, new_weight)
    player.collect_item(item1)
    inventory(player.items)

def run(player):
    for item_run in player.items:
        if item_run.name == "Water Bottle" and item_run.quanity == 100:
            player.items.remove(item_run)
            break
    inventory (player.items)

def take(player):
    item_two = input("What item do you want to collect? ")
    weight = int(input("What is the quanity of the item? "))
    item_two = Item(item_two, weight)
    player.collect_item(item_two)
    print("Check the items in your bag:") 
    inventory(player.items)


def harvest(player):
    item_three = Item("Crops 🌾", 300)
    player.collect_item(item_three)
    inventory(player.items)

   


