from unreliable_car import Unreliable

def main():
    import random
    name = input("Name of your Car:  ")
    fuel = int(input("Amount of fuel in your car:  "))
    reliability = random.randint(0, 101)
    user_car = Unreliable(name, fuel, reliability)
    distance = float(input("The distance you would like to drive with your car:  "))
    print(user_car)
    print(user_car.drive(distance))


main()