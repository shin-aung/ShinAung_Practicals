from taxi import Taxi

def main():
    my_taxi = Taxi("Prisu 1", 100)
    print(my_taxi)
    print(f"My car has driven {my_taxi.drive(40)}km.")
    print(f"The cost of the distanc is {my_taxi.get_fare()}")
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(f"{my_taxi} \nThe cost of the distance is {my_taxi.get_fare()}")


main()