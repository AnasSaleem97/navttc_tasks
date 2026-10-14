# Task 21 - User Defined Functions
# Reference: https://www.geeksforgeeks.org/functions-in-python/

def greet(name="Abubakar"):
    print(f"Welcome, {name}!")

greet()
greet("Ali")

def calculate_grade(marks):
    if marks >= 80:
        return "A"
    elif marks >= 60:
        return "B"
    else:
        return "C"

grade = calculate_grade(85)
print("Grade for 85:", grade)

def get_stats(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return total, average

scores = [78, 85, 92, 88]
s_total, s_avg = get_stats(scores)
print(f"Total: {s_total}, Average: {s_avg}")

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

print("Is 17 prime?", is_prime(17))
print("Is 20 prime?", is_prime(20))
