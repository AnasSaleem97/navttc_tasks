# Task 12 - While Loops
# Reference: https://www.geeksforgeeks.org/python-while-loops/

i = 1
while i <= 5:
    print(i)
    i += 1

count = 10
while count > 0:
    print(count, end=" ")
    count -= 1
print()

total = 0
n = 1
while n <= 100:
    total += n
    n += 1
print("Sum 1 to 100:", total)

answer = ""
while answer != "quit":
    answer = input("Type something (quit to stop): ")
    print("You said:", answer)

x = 0
while True:
    print(x)
    x += 1
    if x == 5:
        break

i = 1
while i <= 3:
    print("Abubakar is studying:", i)
    i += 1
else:
    print("Done studying")
