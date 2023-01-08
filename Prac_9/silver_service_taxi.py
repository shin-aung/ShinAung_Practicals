from taxi import Taxi


class SilverServiceTaxi(Taxi):
    def __init__(self, name, fuel, price_per_km, flagfall):
        super().__init__(name, fuel)
        self.price_per_km = price_per_km
        self.flagfall = flagfall

    def __str__(self):
        return f"{super().__str__()} plus flagfall of ${self.flagfall}"

    def get_fare(self, fanciness):
        return super().get_fare() * fanciness + self.flagfall