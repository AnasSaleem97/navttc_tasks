# Task 42 - Pandas Getting Started
# Reference: https://www.w3schools.com/python/pandas_getting_started.asp

import pandas as pd

print("Pandas successfully imported!")
print("Installed Version:", pd.__version__)

cars_data = {
    "Brand": ["Toyota", "Honda", "Ford"],
    "Passing": [3, 7, 2]
}

my_var = pd.DataFrame(cars_data)
print("\nAbubakar's First DataFrame:\n", my_var)
