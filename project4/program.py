class Player:
    def __init__(self, user_name, location):
        self.user_name = user_name
        self.location = location
        self.list_of_items =[]
    def move(self, destination):
        self.location = destination
    def collect_item (self, item):
        self.list_of_items.append(item)

class Room:
    def __init__ (self, room_name, item=None):
        self.room_name = room_name   
        self.item = item            
class Item:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

room1 = Room("Forest")
room2= Room ("River")
room3 = Room ("Cave")
player1 = Player("Jane",room2)

location = input("Enter the location: ")
item = input("Enter the item: ")
list_of_item = []
while item != "":
    if player1.location != "":
        new_item = Item(item, 100)
        player1.collect_item(new_item)
    else:
        print("Please input the location")
        location = input("Enter the location: ")
        item = input("Enter the item: ")

    item = input("Enter the item: ")

item1 = Item("Compass", 120)
player1.collect_item(item1)

player1.move(room1)

player1.collect_item(item1)
print(f"User name: {player1.user_name}.")
print(f"The location is: {player1.location.room_name}.")
print(f"The list of item: {[item.name for item in player1.list_of_items]}")
print(f"The weight of item is: {item1.weight}.")
