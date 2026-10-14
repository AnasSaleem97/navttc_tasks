# Task 44 - Pandas DataFrame
# Reference: https://www.w3schools.com/python/pandas_dataframes.asp

import pandas as pd

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

df = pd.DataFrame(data)
print("Basic DataFrame:\n", df)

print("\nLocate row 0 using loc:")
print(df.loc[0])

print("\nLocate rows 0 and 1:")
print(df.loc[[0, 1]])

df_indexed = pd.DataFrame(data, index=["day1", "day2", "day3"])
print("\nDataFrame with Named Index for Abubakar:\n", df_indexed)
print("\nLocate 'day2':\n", df_indexed.loc["day2"])
