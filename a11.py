# Python program to check if a number is even or odd

while True:
    try:
        num = int(input("Enter a number (or type -1 to exit): "))
        if num == -1:
            print("Exiting program.")
            break
        elif num % 2 == 0:
            print(f"{num} is Even.")
        else:
            print(f"{num} is Odd.")
    except ValueError:
        print("Please enter a valid integer.")
