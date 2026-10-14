# Task 30 - NumPy Array Slicing
# Reference: https://www.w3schools.com/python/numpy_array_slicing.asp

import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60, 70])

print("Slice 1 to 5:", arr[1:5])
print("Slice 4 to end:", arr[4:])
print("Slice beginning to 4:", arr[:4])
print("Step slice with step 2:", arr[::2])
print("Negative slice (-3 to -1):", arr[-3:-1])

matrix = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print("2nd element from both rows:", matrix[0:2, 1])
print("From both rows, slice index 1 to 4:\n", matrix[0:2, 1:4])
print("Abubakar's slice check complete.")
