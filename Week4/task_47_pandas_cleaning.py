# Task 47 - Pandas Data Cleaning Techniques
# Reference: https://www.w3schools.com/python/pandas_cleaning.asp

import pandas as pd
import os

csv_path = os.path.join(os.path.dirname(__file__), "data.csv")
df = pd.read_csv(csv_path)

print("Null values per column before cleaning:")
print(df.isnull().sum())

mean_calories = df["Calories"].mean()
df["Calories"].fillna(mean_calories, inplace=True)
print("\nFilled missing Calories with mean:", round(mean_calories, 1))

print("Duplicate rows count before cleaning:", df.duplicated().sum())
df.drop_duplicates(inplace=True)

print("Cleaned DataFrame for Abubakar:\n", df.head())
print("\nFinal shape after cleaning:", df.shape)
