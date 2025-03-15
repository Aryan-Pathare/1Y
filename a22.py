class Vehicle:
    def __init__(self, vehicle_type, rent_price, stock):
        self.vehicle_type = vehicle_type
        self.rent_price = rent_price
        self.stock = stock

    def display_availability(self):
        print(f"\nAvailable {self.vehicle_type}: {self.stock} units | Rent per day: Rs {self.rent_price}\n")


class RentalAgency(Vehicle):
    def __init__(self, agency_name, vehicle_type, rent_price, stock):
        super().__init__(vehicle_type, rent_price, stock)
        self.agency_name = agency_name

    def rent_vehicle(self, num_vehicles):
        if num_vehicles > self.stock:
            print("\nSorry, not enough stock available. Try again!\n")
            return False
        else:
            self.stock -= num_vehicles
            return True

    def get_rental_period(self):
        while True:
            try:
                days = int(input("Enter rental period (days): "))
                if days > 0:
                    return days
                else:
                    print("Please enter a valid number of days.")
            except ValueError:
                print("Invalid input! Please enter a number.")

    def return_vehicle(self, num_vehicles):
        self.stock += num_vehicles
        print(f"\nThank you for returning {num_vehicles} {self.vehicle_type}(s). Updated stock: {self.stock}\n")


class RentalTransaction(RentalAgency):
    def __init__(self, agency_name, vehicle_type, rent_price, stock):
        super().__init__(agency_name, vehicle_type, rent_price, stock)

    def calculate_amount(self, num_vehicles, rental_days):
        return num_vehicles * self.rent_price * rental_days


# Initializing rental agencies
car_rental = RentalTransaction("Star", "Car", 25, 200)
bus_rental = RentalTransaction("Royal", "Bus", 50, 100)

print("\n===== WELCOME TO THE VEHICLE RENTAL SYSTEM =====\n")
while True:
    print("1. Rent a Car\n2. Rent a Bus\n3. Check Vehicle Availability\n4. Return a Vehicle\n5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        car_rental.display_availability()
        num = int(input("Enter the number of Cars to rent: "))
        if car_rental.rent_vehicle(num):
            days = car_rental.get_rental_period()
            amount = car_rental.calculate_amount(num, days)
            print(f"\nYour order for {num} Cars from {car_rental.agency_name} is confirmed. Total: Rs {amount}\n")

    elif choice == "2":
        bus_rental.display_availability()
        num = int(input("Enter the number of Buses to rent: "))
        if bus_rental.rent_vehicle(num):
            days = bus_rental.get_rental_period()
            amount = bus_rental.calculate_amount(num, days)
            print(f"\nYour order for {num} Buses from {bus_rental.agency_name} is confirmed. Total: Rs {amount}\n")

    elif choice == "3":
        car_rental.display_availability()
        bus_rental.display_availability()

    elif choice == "4":
        vehicle_type = input("Enter vehicle type to return (Car/Bus): ").strip().lower()
        num = int(input("Enter the number of vehicles to return: "))
        if vehicle_type == "car":
            car_rental.return_vehicle(num)
        elif vehicle_type == "bus":
            bus_rental.return_vehicle(num)
        else:
            print("\nInvalid vehicle type! Please enter either 'Car' or 'Bus'.\n")

    elif choice == "5":
        print("\nThank you for using our service. Have a great day!\n")
        break

    else:
        print("\nInvalid choice! Please try again.\n")