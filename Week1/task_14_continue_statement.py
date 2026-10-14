# Task 14 - Continue Statement
# Reference: https://www.geeksforgeeks.org/python-continue-statement/

for i in range(1, 11):
    if i % 2 != 0:
        continue
    print(i)

n = 0
while n < 10:
    n += 1
    if n % 3 == 0:
        continue
    print(n)

scores = [85, -5, 90, -2, 78, 0, 95]
for s in scores:
    if s <= 0:
        continue
    print("Abubakar's score:", s)
