class Player:
    def __init__(self, user_name, location):
        self.user_name = user_name
        self.location = location
        self.list_of_item =[]
    def move(self, destination):
        self.location = destination
    def collect_item (self, item):
        self.list_of_item.append(item)

player_name = input("   - Name of gamer: ")
location = input("   - Location: ")
player1 = Player(player_name, location)
