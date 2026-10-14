# Task 50 - Standard Deviation and Variance
# Reference: https://www.w3schools.com/python/python_ml_standard_deviation.asp

import numpy as np

marks = [86, 87, 88, 86, 93, 85, 84]

std_dev = np.std(marks)
variance = np.var(marks)

print("Data values:", marks)
print("Standard Deviation:", round(std_dev, 2))
print("Variance:", round(variance, 2))
print("Abubakar's standard deviation squared equals variance:", np.isclose(std_dev ** 2, variance))
