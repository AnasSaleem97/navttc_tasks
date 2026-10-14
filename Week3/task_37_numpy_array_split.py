# Task 37 - NumPy Array Splitting
# Reference: https://www.w3schools.com/python/numpy_array_split.asp

import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])
split_3 = np.array_split(arr, 3)

print("Original array:", arr)
print("Split into 3 parts:")
for part in split_3:
    print(part)

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
matrix_split = np.array_split(matrix, 2)

print("2-D split part 1:\n", matrix_split[0])
print("2-D split part 2 for Abubakar:\n", matrix_split[1])

col_split = np.hsplit(matrix, 3)
print("Horizontal split (column 1):\n", col_split[0])
