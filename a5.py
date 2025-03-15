def calculate_simple_interest(principal, rate, time):
    simple_interest = (principal * rate * time) / 100
    return simple_interest

# Prompt user for inputs
principal = float(input("Enter the Principal Amount: "))
rate = float(input("Enter the Rate of Interest (in %): "))
time = float(input("Enter the Time Period (in years): "))

# Calculate simple interest
simple_interest = calculate_simple_interest(principal, rate, time)

# Display the result
print(f"Principal Amount: {principal:.2f}")
print(f"Rate of Interest: {rate:.2f}%")
print(f"Time Period: {time:.2f} years")
print(f"Simple Interest: {simple_interest:.2f}")
