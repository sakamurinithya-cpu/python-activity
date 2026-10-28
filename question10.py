#Bus Passenger Occupancy
capacity = int(input("Enter bus capacity: "))
passengers = 0

if capacity <= 0:
    print("Invalid bus capacity")
else:
    stops = int(input("Enter number of stops: "))

    if stops < 0:
        print("Invalid number of stops")
    else:
        for i in range(stops):
            print("\nStop", i + 1)

            boarding = int(input("Passengers boarding: "))
            leaving = int(input("Passengers leaving: "))

            if boarding < 0 or leaving < 0 or leaving > passengers:
                print("Invalid passenger data")
                continue

            passengers = passengers - leaving + boarding

            print("Current passengers =", passengers)

            if passengers > capacity:
                print("Warning: Bus capacity exceeded!")
            else:
                print("Bus is within capacity")

        print("\nFinal passenger count =", passengers)