class Vehicle(object):
    def __init__(self, speed, mileage, color = 'white'):
        self.speed = speed
        self.mileage = mileage
        self.color = color
        self.seating_capacity = None

    def assign_seating_capacity(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def display_properties(self):
        print(f"Speed: {self.speed}\nMileage: {self.mileage}\nSeating capacity: {self.seating_capacity}\nColor: {self.color}")

ford = Vehicle(170, 200, 'blue')
ford.assign_seating_capacity(4)
ford.display_properties()