from tire import Tire

class CarriganTire(Tire):
    def __init__(self, tire_array):
        self.tire_array = tire_array

    def needs_service(self):
        for tire in self.tire_array:
            if tire >= .9:
                return True
        return False