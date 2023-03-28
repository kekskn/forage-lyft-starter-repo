from tire.tire import Tire


class CarriganTire(Tire):
    def __init__(self, tire_wear=[0, 0, 0, 0]):
        if len(tire_wear) != 4:
            raise ValueError("Expected list of four values")
        if not all(0 <= value <= 1 for value in tire_wear):
            raise ValueError("Values must be between 0 and 1 inclusive")
        self.tire_wear = tire_wear

    def needs_service(self):
        count = sum(value >= 0.9 for value in self.tire_wear)
        if count != 1:
            return False
        else:
            return True
