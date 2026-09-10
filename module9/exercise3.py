
class Car:
    def __init__(self, license_plate, maximum_speed):
        self.license_plate = license_plate
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0
    
    def accelerate (self, change):
        if self.current_speed + change >= self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed + change <= 0:
            self.current_speed = 0
        else:
            self.current_speed += change

    def drive (self, hours):
        if (self.current_speed * hours) + self.travelled_distance > self.travelled_distance:
            self.travelled_distance = (self.current_speed * hours) + self.travelled_distance
        else:
            self.travelled_distance = self.travelled_distance

car1 = Car("ABC-123", 142)

car1.accelerate(60)
print(f"Current speed: {car1.current_speed} km/h")

print(f"Initial distance: {car1.travelled_distance} km")

car1.current_speed = 60
car1.drive(1.5)

print(f"Distance after driving 1.5 hours at 60 km/h: {car1.travelled_distance} km")