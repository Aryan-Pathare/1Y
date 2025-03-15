# Python program to print a pyramid pattern

# Get number of rows from the user
rows = int(input("Enter the number of rows: "))

# Printing the pyramid pattern
for i in range(1, rows + 1):
    print(" " * (rows - i) + "* " * i)
