# Task 46 - Pandas Data Analyzing
# Reference: https://www.w3schools.com/python/pandas_analyzing.asp

import pandas as pd
import os

csv_path = os.path.join(os.path.dirname(__file__), "data.csv")
df = pd.read_csv(csv_path)

print("--- Head (first 5 rows) ---")
print(df.head())

print("\n--- Tail (last 3 rows) ---")
print(df.tail(3))

print("\n--- Summary Statistics (describe) ---")
print(df.describe())

print("\n--- Dataset Info for Abubakar ---")
df.info()
