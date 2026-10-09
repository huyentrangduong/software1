
class Player:
    def __init__(self, player_name, location):
        self.player_name = player_name
        self.location = location
        self.items =[]
        self.quanity = 0
    def collect_item(self,item):
        self.items.append(item)

    
