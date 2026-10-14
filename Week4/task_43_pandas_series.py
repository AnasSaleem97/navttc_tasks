# Task 43 - Pandas Series Data
# Reference: https://www.w3schools.com/python/pandas_series.asp

import pandas as pd

nums = [10, 20, 30]
s1 = pd.Series(nums)
print("Basic Series:\n", s1)
print("First item:", s1[0])

s2 = pd.Series(nums, index=["a", "b", "c"])
print("\nSeries with custom index:\n", s2)
print("Item at label 'b':", s2["b"])

calories = {"Day 1": 420, "Day 2": 380, "Day 3": 390}
s3 = pd.Series(calories)
print("\nAbubakar's Calorie Series:\n", s3)
print("Calories on Day 2:", s3["Day 2"])
