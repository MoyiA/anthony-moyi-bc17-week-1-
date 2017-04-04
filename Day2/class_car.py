class Car():
    def __init__(self, name = "General", model = "GM", car_type = "Saloon"):
        self.name = name
        self.model = model
        self.car_type = car_type
        if model == "Truck":
            self.num_of_wheels = 8
        else:
            self.num_of_wheels = 4

        self.speed = 0
    
    def drive(self, n):
        pass

    def is_saloon(self):
        if self.car_type == "Saloon":
            return True
        else:
            return False



