# Task 13 - Break Statement
# Reference: https://www.geeksforgeeks.org/python-break-statement/

for i in range(1, 11):
    if i == 6:
        break
    print(i)

n = 0
while True:
    n += 1
    print(n)
    if n == 5:
        break

names = ["Sara", "Ahmed", "Abubakar", "Fatima"]
for name in names:
    if name == "Abubakar":
        print("Found Abubakar!")
        break

for i in range(3):
    for j in range(3):
        if j == 1:
            break
        print(i, j)
