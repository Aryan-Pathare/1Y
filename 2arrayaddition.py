import numpy as np

# Create two arrays of the same shape
array1 = np.array([[1, 2, 3], [4, 5, 6]])
array2 = np.array([[7, 8, 9], [10, 11, 12]])

# Perform element-wise operations
addition = array1 + array2
subtraction = array1 - array2
multiplication = array1 * array2
division = array1 / array2

print("Element-wise Addition:\n", addition)
print("\nElement-wise Subtraction:\n", subtraction)
print("\nElement-wise Multiplication:\n", multiplication)
print("\nElement-wise Division:\n", division)

# Dot product of two vectors
vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])
dot_product = np.dot(vector1, vector2)

print("\nDot Product of the vectors:\n", dot_product)

# Cross product of two vectors
cross_product = np.cross(vector1, vector2)

print("\nCross Product of the vectors:\n", cross_product)
