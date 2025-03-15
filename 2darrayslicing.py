# create a 2D array
import numpy as np
array1 = np.array([[1, 3, 5, 7], [9, 11, 13, 15]])


print(array1[0:1, 1:3])

#-----------------------------------------------------
import numpy as np

# create a 2D array 
array1 = np.array([[1, 3, 5, 7], [9, 11, 13, 15],[2, 4, 6, 8]])


# slice the array to get the first two rows and columns
subarray1 = array1[:2, :2]

# slice the array to get the last two rows and columns
subarray2 = array1[1:3, 2:4]

# print the subarrays
print("First Two Rows and Columns: \n",subarray1)
print("Last two Rows and Columns: \n",subarray2)

#--------------------------------------------------reshaping 1d-2d
import numpy as np

array1 = np.array([1, 3, 5, 7, 2, 4, 6, 8])

# reshape a 1D array into a 2D array 
# with 2 rows and 4 columns
result = np.reshape(array1, (2, 4))
print(result)
#----------------------------------------------------------1d-3d
import numpy as np

# create a 1D array
array1 = np.array([1, 3, 5, 7, 2, 4, 6, 8])

# reshape the 1D array to a 3D array
result = np.reshape(array1, (2, 2, 2))

# print the new array
print("1D to 3D Array: \n",result)

#-----------------------------------------------Flatten
import numpy as np

# flatten 2D array to 1D
array1 = np.array([[1, 3], [5, 7], [9, 11]])
result1 = np.reshape(array1, -1)
print("Flattened 2D array:", result1)

# flatten 3D array to 1D
array2 = np.array([[[1, 3], [5, 7]], [[2, 4], [6, 8]]])
result2 = np.reshape(array2, -1)
print("Flattened 3D array:", result2)

