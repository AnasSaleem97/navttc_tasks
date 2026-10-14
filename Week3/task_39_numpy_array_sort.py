# Task 39 - NumPy Array Sorting
# Reference: https://www.w3schools.com/python/numpy_array_sort.asp

import numpy as np

nums = np.array([34, 12, 89, 5, 23, 77])
sorted_nums = np.sort(nums)
print("Original:", nums)
print("Sorted numbers for Abubakar:", sorted_nums)

fruits = np.array(["banana", "apple", "mango", "orange"])
print("Sorted strings:", np.sort(fruits))

bools = np.array([True, False, True, False])
print("Sorted booleans:", np.sort(bools))

mat = np.array([[5, 2, 8], [9, 1, 4]])
print("Sorted 2-D array (each row sorted):\n", np.sort(mat))
