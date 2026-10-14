# Task 40 - NumPy Random Technique
# Reference: https://www.w3schools.com/python/numpy_random.asp

from numpy import random

rand_int = random.randint(100)
rand_float = random.rand()
print("Random integer (0-100):", rand_int)
print("Random float (0-1):", round(rand_float, 4))

rand_arr = random.randint(10, 50, size=(5,))
print("Random 1-D array (5 ints):", rand_arr)

rand_matrix = random.randint(1, 20, size=(3, 3))
print("Random 3x3 matrix:\n", rand_matrix)

choices = ["Python", "Machine Learning", "Deep Learning", "Data Science"]
selected = random.choice(choices)
print("Random course picked for Abubakar:", selected)

norm_sample = random.normal(loc=50, scale=5, size=5)
print("Normal distribution sample:", np_sample := [round(x, 2) for x in norm_sample])
