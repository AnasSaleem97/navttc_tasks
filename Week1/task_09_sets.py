# Task 09 - Sets

subjects = {"Math", "Python", "AI", "SQL", "Python"}
print(subjects)

subjects.add("Statistics")
subjects.update(["Power BI", "Excel"])
print(subjects)

subjects.remove("Math")
subjects.discard("Java")
print(subjects)

print(len(subjects))
print("Python" in subjects)

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

print(a | b)
print(a & b)
print(a - b)
print(a ^ b)

small = {1, 2}
print(small.issubset(a))
print(a.issuperset(small))
