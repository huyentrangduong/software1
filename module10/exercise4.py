import random

class Car:
    def __init__(self, license_plate, maximum_speed):
        self.license_plate = license_plate
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        self.current_speed += speed_change
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        distance_travelled = self.current_speed * hours
        self.travelled_distance += distance_travelled

class Race:
    def __init__(self,name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars
    
    def hour_passes (self):
        for car in self.cars:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)
           
    def print_status(self):
        for car in self.cars:
            print(
                car.license_plate,
                car.maximum_speed,
                car.current_speed,
                car.travelled_distance
            )        
    def race_finished (self):
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return True 
    
        return False
        print(f"\nRace finished initially: {Race.race_finished()}")
        

list_of_car =[]

list_of_car.append(Car("ABC-123", 100))
list_of_car.append(Car("DEF-456", 100))
list_of_car.append(Car("GHJ-789", 100))
