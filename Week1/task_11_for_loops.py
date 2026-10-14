# Task 11 - For Loops
# Reference: https://www.geeksforgeeks.org/python-for-loops/

courses = ["Python", "SQL", "AI", "Power BI"]
for course in courses:
    print(course)

for i in range(5):
    print(i)

for i in range(1, 11):
    print(i, end=" ")
print()

for i in range(2, 21, 2):
    print(i, end=" ")
print()

for letter in "Abubakar":
    print(letter, end=" ")
print()

total = 0
for n in range(1, 11):
    total += n
print("Sum 1-10:", total)

for i in range(1, 4):
    for j in range(1, 4):
        print(i * j, end="\t")
    print()
