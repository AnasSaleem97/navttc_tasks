# Task 38 - NumPy Array Searching
# Reference: https://www.w3schools.com/python/numpy_array_search.asp

import numpy as np

arr = np.array([10, 25, 40, 25, 50, 25, 70])

matches = np.where(arr == 25)
print("Indices where value is 25:", matches[0])

even_indices = np.where(arr % 2 == 0)
print("Indices with even numbers:", even_indices[0])

sorted_arr = np.array([10, 20, 30, 40, 50])
insert_pos = np.searchsorted(sorted_arr, 35)
print("Position to insert 35 for Abubakar to keep array sorted:", insert_pos)
