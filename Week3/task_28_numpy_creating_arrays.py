# Task 28 - NumPy Creating Arrays
# Reference: https://www.w3schools.com/python/numpy_creating_arrays.asp

import numpy as np

arr0 = np.array(42)
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
arr3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

print("0-D Array:", arr0)
print("1-D Array for Abubakar:", arr1)
print("2-D Array:\n", arr2)

print("Dimensions:")
print("arr0 ndim:", arr0.ndim)
print("arr1 ndim:", arr1.ndim)
print("arr2 ndim:", arr2.ndim)
print("arr3 ndim:", arr3.ndim)
