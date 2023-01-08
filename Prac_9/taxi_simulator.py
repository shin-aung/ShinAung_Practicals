from silver_service_taxi import SilverServiceTaxi
from taxi import Taxi
def main():
    taxis = []
    taxis_choices = []
    prius = Taxi("Prius", 100)
    limo = SilverServiceTaxi("Limo", 100, 2.46, 4.50)
    hummer = SilverServiceTaxi("Hummer", 200, 4.92, 4.50)
    taxis.append(prius)
    taxis.append(limo)
    taxis.append(hummer)
    print("Lets's drive!")
    CHOICES = "q)uit, c)hoose taxi, d)rive"
    print(CHOICES)
    choice = input(">>> ").upper()
    bill = 0
    while choice != "Q":
        if choice == "C":
            print("Taxis available:")
            for i in range(0, len(taxis), 1):
                print(f"{i} - {taxis[i]}")
            taxi_choice = int(input("Choose taxi: "))
            if int(taxi_choice) >= int(len(taxis)):
                print("Invalid taxi choice")
            else:
                taxis_choices.append(taxis[int(taxi_choice)])
            print(f"Bill to date: ${float(bill)}")
        elif choice == "D":
            if taxis_choices == "":
                print("You need to choose a taxi before you can drive")
            else:
                distance = int(input("Drive how far? "))
                taxis_choices[0].drive(distance)
                bill += taxis_choices[0].get_fare()
                print(f"Your {taxis_choices[0].name} trip cost you ${taxis_choices[0].get_fare()}")
                taxis_choices.remove(taxis_choices[0])
            print(f"Bill to date: ${float(bill)}")
        else:
            print("Invalid option")
        print(CHOICES)
        choice = input(">>> ").upper()
    print(f"Total trip cost: ${bill}")
    print("Taxis are now:")
    for i in range(0, len(taxis), 1):
        print(f"{i} - {taxis[i]}")

main()