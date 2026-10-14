# Task 05 - Input and Type Casting

name = input("Enter your name: ")
age = input("Enter your age: ")
age = int(age)

print("Hello", name)
print("Next year you will be", age + 1)

price = float(input("Enter price: "))
qty = int(input("Enter quantity: "))
print("Total:", price * qty)

print(type(name))
print(type(age))
print(type(price))
