import random
class Car:
    created = 0

    def __init__(self, license_plate, maximum_speed):
        self.license_plate = license_plate
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0
        Car.created = Car.created + 1
        

    def accelerate (self, change):
        if self.current_speed + change >= self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed + change <= 0:
            self.current_speed = 0
        else:
            self.current_speed += change

    def drive (self, hours):
        self.travelled_distance = (self.current_speed * hours) + self.travelled_distance



def race (cars):
    race_continues = True
    while race_continues:
        for car in cars:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)
            if car.travelled_distance >= 10000:
                race_continues = False
                break
    return cars
 
list_of_car =[]

list_of_car.append(Car("ABC-123", 100))
list_of_car.append(Car("DEF-456", 100))
list_of_car.append(Car("GHJ-789", 100))


result = race(list_of_car)
