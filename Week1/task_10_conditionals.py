# Task 10 - Conditional Execution

marks = int(input("Enter Abubakar's marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
else:
    print("Grade F")

age = 20
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible")

num = int(input("Enter a number: "))
if num > 0:
    if num % 2 == 0:
        print("Positive even")
    else:
        print("Positive odd")
elif num < 0:
    print("Negative number")
else:
    print("Zero")

status = "Pass" if marks >= 50 else "Fail"
print(status)
