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
            
class Building:
    def __init__(self, bottom_floor, top_floor, elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = []
        for i in range(elevators):
            self.elevators.append(Elevator(bottom_floor, top_floor))
        
    def run_elevator(self,elevator_number, destination_floor):
        self.elevators[elevator_number].go_to_floor(destination_floor)

h = Elevator(1, 10)
h.go_to_floor(1)
h.go_to_floor(5)

building = Building(1, 10, 3)
building.run_elevator(0, 5)
building.run_elevator(1, 3)
building.run_elevator(2, 8)