import numpy as np

# Creating a 1D NumPy Array
arr_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:")
print(arr_1d)

# Creating a 2D NumPy Array
arr_2d = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print("\n2D Array:")
print(arr_2d)

# Creating a 3D NumPy Array
arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("\n3D Array:")
print(arr_3d)

# Reshaping 1D Array to 2D (1 row, 5 columns)
reshaped_2d = arr_1d.reshape(1, 5)
print("\nReshaped 1D to 2D:")
print(reshaped_2d)

# Reshaping 1D Array to 3D (1 block, 5 rows, 1 column)
reshaped_3d = arr_1d.reshape(5, 1, 1)
print("\nReshaped 1D to 3D:")
print(reshaped_3d)

# Slicing in 1D Array (Extracting elements from index 1 to 3)
print("\nSliced 1D Array (Elements 2 to 4):", arr_1d[1:4])

# Slicing in 2D Array (Extracting first two rows and last column)
print("\nSliced 2D Array (First two rows, last column):")
print(arr_2d[:2, 2])

# Indexing in 3D Array (Accessing specific element)
print("\nAccessing Element at (1,0,1) in 3D Array:", arr_3d[1, 0, 1])
