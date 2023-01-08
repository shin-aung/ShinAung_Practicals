from silver_service_taxi import SilverServiceTaxi


def main():
    silver_service_taxi = SilverServiceTaxi("Hummer", 200, 4.92, 4.50)
    print(silver_service_taxi)
    silver_service_taxi.drive(18)
    print(silver_service_taxi.get_fare(2))
    print(silver_service_taxi)

main()