from tire import Tire

class OctoprimeTire(Tire):
    def __init__(self, tire_array):
        self.tire_array = tire_array

    def needs_service(self):
        tire_condition_sum = 0
        for tire in self.tire_array:
            tire_condition_sum += tire
        return tire_condition_sum > 3