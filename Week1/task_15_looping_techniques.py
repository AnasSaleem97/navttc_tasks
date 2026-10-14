# Task 15 - Looping Techniques
# Reference: https://www.geeksforgeeks.org/looping-techniques-python/

subjects = ["Math", "Physics", "Python", "AI"]
marks = [85, 90, 95, 88]

for i, sub in enumerate(subjects, 1):
    print(i, sub)

for sub, m in zip(subjects, marks):
    print("Abubakar:", sub, "->", m)

nums = [10, 45, 23, 78, 12]
for n in sorted(nums):
    print(n, end=" ")
print()

for s in reversed(subjects):
    print(s, end=" ")
print()

student = {"name": "Abubakar", "age": 21, "city": "Lahore"}
for key, value in student.items():
    print(key, ":", value)
