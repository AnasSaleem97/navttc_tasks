# Task 45 - Pandas Open CSV Files
# Reference: https://www.w3schools.com/python/pandas_csv.asp

import pandas as pd
import os

csv_path = os.path.join(os.path.dirname(__file__), "data.csv")
df = pd.read_csv(csv_path)

print("Loaded CSV successfully!")
print("\nFirst few rows:\n", df.head())

print("\nFull DataFrame using to_string():\n")
print(df.to_string())

print(f"\nTotal rows loaded for Abubakar: {len(df)}")
