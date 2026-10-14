# Task 32 - NumPy Copy vs View
# Reference: https://www.w3schools.com/python/numpy_copy_vs_view.asp

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

arr_copy = arr.copy()
arr_copy[0] = 99

print("Original array after modifying copy:", arr)
print("Modified copy:", arr_copy)

arr_view = arr.view()
arr_view[0] = 77

print("Original array after modifying view:", arr)
print("Modified view:", arr_view)

print("Copy base check (owns data?):", arr_copy.base)
print("View base check for Abubakar (owns data?):", arr_view.base is not None)
