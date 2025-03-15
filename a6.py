def arithmetic_operations(num1, num2):
    print(f"Addition: {num1} + {num2} = {num1 + num2}")
    print(f"Subtraction: {num1} - {num2} = {num1 - num2}")
    print(f"Multiplication: {num1} * {num2} = {num1 * num2}")
    if num2 != 0:
        print(f"Division: {num1} / {num2} = {num1 / num2}")
        print(f"Modulus: {num1} % {num2} = {num1 % num2}")
    else:
        print("Division and modulus by zero are not allowed.")

# Prompt user for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform arithmetic operations
arithmetic_operations(num1, num2)
