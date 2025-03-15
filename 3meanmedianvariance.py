import numpy as np

# Example array
data = np.array([10, 20, 30, 40, 50])

# Calculate mean
mean = np.mean(data)
print(f"Mean: {mean}")

# Calculate median
median = np.median(data)
print(f"Median: {median}")

# Calculate standard deviation
std_dev = np.std(data)
print(f"Standard Deviation: {std_dev}")

# Calculate variance
variance = np.var(data)
print(f"Variance: {variance}")

# Correlation coefficients
# For correlation, we need at least two datasets
data2 = np.array([15, 25, 35, 45, 55])
correlation = np.corrcoef(data, data2)
print(f"Correlation Coefficients:\n{correlation}")
