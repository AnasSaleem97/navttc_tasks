# Task 36 - NumPy Matrix Joining
# Reference: https://www.w3schools.com/python/numpy_array_join.asp

import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
joined_1d = np.concatenate((arr1, arr2))
print("1-D joined:", joined_1d)

mat1 = np.array([[1, 2], [3, 4]])
mat2 = np.array([[5, 6], [7, 8]])

join_rows = np.concatenate((mat1, mat2), axis=0)
join_cols = np.concatenate((mat1, mat2), axis=1)

print("Concatenate along axis=0 (rows):\n", join_rows)
print("Concatenate along axis=1 (cols):\n", join_cols)

h_stacked = np.hstack((mat1, mat2))
v_stacked = np.vstack((mat1, mat2))
print("HStack:\n", h_stacked)
print("VStack for Abubakar:\n", v_stacked)
