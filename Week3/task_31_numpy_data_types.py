# Task 31 - NumPy Data Types
# Reference: https://www.w3schools.com/python/numpy_data_types.asp

import numpy as np

arr_int = np.array([1, 2, 3, 4])
arr_str = np.array(["apple", "banana", "cherry"])
arr_float = np.array([1.1, 2.2, 3.3])

print("Integer array dtype:", arr_int.dtype)
print("String array dtype:", arr_str.dtype)
print("Float array dtype:", arr_float.dtype)

arr_i4 = np.array([1, 2, 3], dtype="i4")
print("Explicit 4-byte int:", arr_i4.dtype)

float_arr = np.array([1.9, 2.1, 3.7])
int_arr = float_arr.astype("i")
bool_arr = np.array([1, 0, 3]).astype(bool)

print("Converted float to int for Abubakar:", int_arr)
print("Converted to bool:", bool_arr)
