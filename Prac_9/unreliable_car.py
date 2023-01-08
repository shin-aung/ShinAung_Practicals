from car import Car


class Unreliable(Car):
    import random
    random_number = random.randint(0, 100)

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        return f"{super().__str__()} The reliability of your car is {self.reliability}."

    def drive(self, distance):
        if Unreliable.random_number < self.reliability:
            super().drive(distance)
            return f"You can travel {distance}km and you can rely on your {self.reliability} reliability. Your new distance trevelled will be {self.odometer}km."
        else:
            return f"You can not travel {distance}km because your reliability which is {self.reliability} is not good enough. Your distance travelled with still be {self.odometer}km."

