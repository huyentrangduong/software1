class Elevator:

    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        self.current_floor += 1

    def floor_down(self):
        self.current_floor -= 1


    def go_to_floor(self, target_floor):

        while self.current_floor < target_floor:
            self.floor_up()

        while self.current_floor > target_floor:
            self.floor_down()


h = Elevator(1, 10)
print("Basic elevator test:")
h.go_to_floor(1)
h.go_to_floor(5)

