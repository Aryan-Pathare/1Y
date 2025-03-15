import numpy as np

while True:
    try:
        # Taking input from user
        data = list(map(float, input("Enter numbers separated by spaces: ").split()))
        if not data:
            raise ValueError("Input cannot be empty. Please enter valid numbers.")
        break
    except ValueError as e:
        print(f"Invalid input: {e}. Please try again.")

# Calculating statistics
mean = np.mean(data)
median = np.median(data)
std_dev = np.std(data, ddof=1)  # Sample standard deviation
variance = np.var(data, ddof=1)  # Sample variance

# Displaying results
print(f"\nMean: {mean}")
print(f"Median: {median}")
print(f"Standard Deviation: {std_dev}")
print(f"Variance: {variance}")
