# Task 29 - NumPy Array Indexing
# Reference: https://www.w3schools.com/python/numpy_array_indexing.asp

import numpy as np

arr1 = np.array([10, 20, 30, 40, 50])
print("First element:", arr1[0])
print("Third element:", arr1[2])
print("Last element:", arr1[-1])

arr2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print("2nd element on 1st row:", arr2[0, 1])
print("4th element on 2nd row:", arr2[1, 3])

arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print("Element at [0, 1, 2]:", arr3[0, 1, 2])

sum_res = arr1[1] + arr1[3]
print("Abubakar's calculated sum (20 + 40):", sum_res)
