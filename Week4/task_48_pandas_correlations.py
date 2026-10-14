# Task 48 - Pandas Data Correlation
# Reference: https://www.w3schools.com/python/pandas_correlations.asp

import pandas as pd
import os

csv_path = os.path.join(os.path.dirname(__file__), "data.csv")
df = pd.read_csv(csv_path)

corr_matrix = df.corr()
print("Correlation Matrix for Abubakar:")
print(corr_matrix)

pulse_cal_corr = corr_matrix.loc["Pulse", "Calories"]
print(f"\nCorrelation between Pulse and Calories: {round(pulse_cal_corr, 3)}")
