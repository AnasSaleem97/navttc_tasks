# Task 33 - NumPy Array Shape
# Reference: https://www.w3schools.com/python/numpy_array_shape.asp

import numpy as np

arr_1d = np.array([1, 2, 3, 4, 5])
arr_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
arr_5d = np.array([1, 2, 3, 4], ndmin=5)

print("1-D Array Shape:", arr_1d.shape)
print("2-D Array Shape (rows, cols):", arr_2d.shape)
print("5-D Array Shape for Abubakar:", arr_5d.shape)

rows, cols = arr_2d.shape
print(f"Matrix has {rows} rows and {cols} columns.")
