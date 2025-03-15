import numpy as np

# Taking input from user
data = list(map(float, input("Enter numbers separated by spaces: ").split()))

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
