# Task 49 - Mean, Median, and Mode
# Reference: https://www.w3schools.com/python/python_ml_mean_median_mode.asp

import numpy as np
from scipy import stats

scores = [85, 90, 78, 92, 88, 90, 85, 90, 95]

mean_val = np.mean(scores)
median_val = np.median(scores)
mode_res = stats.mode(scores)

print("Scores list:", scores)
print("Mean score for Abubakar:", mean_val)
print("Median score:", median_val)
print("Mode score:", mode_res.mode)
