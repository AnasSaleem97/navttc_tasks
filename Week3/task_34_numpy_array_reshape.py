# Task 34 - NumPy Array Reshape
# Reference: https://www.w3schools.com/python/numpy_array_reshape.asp

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

arr_2d = arr.reshape(4, 3)
print("Reshaped to 4x3:\n", arr_2d)

arr_3d = arr.reshape(2, 3, 2)
print("Reshaped to 2x3x2:\n", arr_3d)

auto_dim = arr.reshape(2, 2, -1)
print("Reshaped with auto dimension (-1):\n", auto_dim)

flattened = arr_2d.reshape(-1)
print("Flattened array for Abubakar:", flattened)
