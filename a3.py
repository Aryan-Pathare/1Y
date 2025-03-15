def rupees_to_dollars(rupees, exchange_rate=83):
    return rupees / exchange_rate

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def inches_to_feet(inches):
    return inches / 12

while True:
    print("\nChoose a conversion:")
    print("1. Rupees to Dollars")
    print("2. Celsius to Fahrenheit")
    print("3. Inches to Feet")
    print("4. Exit")
    
    choice = int(input("Enter choice (1/2/3/4): "))
    
    if choice == 1:
        rupees = float(input("Enter amount in Rupees: "))
        print(f"{rupees} INR = {rupees_to_dollars(rupees):.2f} USD")
    elif choice == 2:
        celsius = float(input("Enter temperature in Celsius: "))
        print(f"{celsius}°C = {celsius_to_fahrenheit(celsius):.2f}°F")
    elif choice == 3:
        inches = float(input("Enter length in Inches: "))
        print(f"{inches} inches = {inches_to_feet(inches):.2f} feet")
    elif choice == 4:
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")
