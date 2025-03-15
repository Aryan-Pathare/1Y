import numpy as np

# create a list named list1
list1 = [2, 4, 6, 8]

# create numpy array using list1
array1 = np.array(list1)

print(array1)

# Output: [2 4 6 8]

#--------------------------------------------------------------------------------------------

import numpy as np

# create numpy array using a list
array1 = np.array([2, 4, 6, 8])
print(array1)

# Output: [2  4  6 8]
#-----------------------------------------------------------------------------------------------
import numpy as np

# create a 2D array with 2 rows and 4 columns
array1 = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8]])

print(array1)

#-------------------------------------------------------------------------------------
import numpy as np

# create a 3D array with 2 "slices", each of 3 rows and 4 columns
array1 = np.array([[[1, 2, 3, 4],
                [5, 6, 7, 8], 
                [9, 10, 11, 12]],
                     
                [[13, 14, 15, 16], 
                 [17, 18, 19, 20], 
                 [21, 22, 23, 24]]])

print(array1)
