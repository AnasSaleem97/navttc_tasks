# Task 41 - Pandas Basics
# Reference: https://www.w3schools.com/python/pandas_tutorial.asp

import pandas as pd

dataset = {
    "student": ["Abubakar", "Hamza", "Zain"],
    "courses": ["AI", "Data Science", "Machine Learning"],
    "score": [92, 85, 88]
}

df = pd.DataFrame(dataset)
print("Pandas version:", pd.__version__)
print("\nDataFrame:\n", df)
