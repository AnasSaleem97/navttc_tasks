# Task 22 - Exception Handling
# Reference: https://www.programiz.com/python-programming/exception-handling

try:
    num1 = 10
    num2 = 0
    ans = num1 / num2
    print(ans)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

try:
    val = int("abc")
except ValueError as e:
    print("Conversion error:", e)

marks = [75, 80, 92]
try:
    print("4th mark:", marks[3])
except IndexError:
    print("Index out of range for Abubakar's list")

try:
    res = 100 / 5
except ZeroDivisionError:
    print("Division error")
else:
    print("Operation succeeded, result:", res)
finally:
    print("Execution completed.")
