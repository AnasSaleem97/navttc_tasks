# Task 17 - Tuple Data Type
# Reference: https://www.programiz.com/python-programming/tuple

info = ("Abubakar", 21, "CS Student", "Pakistan")
print("Tuple:", info)
print("Name:", info[0])
print("Role:", info[2])

print("Slice:", info[1:3])

nums = (1, 2, 3, 2, 4, 2, 5)
print("Count of 2:", nums.count(2))
print("Index of 3:", nums.index(3))

name, age, degree, country = info
print("Unpacked:", name, "studies", degree)
print("Length of tuple:", len(info))
