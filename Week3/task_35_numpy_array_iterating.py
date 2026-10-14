# Task 35 - NumPy Array Iterating
# Reference: https://www.w3schools.com/python/numpy_array_iterating.asp

import numpy as np

arr1 = np.array([10, 20, 30])
for x in arr1:
    print("1-D item:", x)

arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print("Iterating 2-D row by row:")
for row in arr2:
    print(row)

print("Iterating through every scalar using nditer:")
for val in np.nditer(arr2):
    print(val, end=" ")
print()

print("Iterating with indices using ndenumerate:")
for idx, val in np.ndenumerate(arr2):
    print(f"Abubakar index {idx} -> {val}")
