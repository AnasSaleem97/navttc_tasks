# Task 08 - Dictionaries

student = {
    "name": "Abubakar",
    "age": 21,
    "course": "AI & Data Science",
    "marks": 88
}

print(student)
print(student["name"])
print(student.get("phone", "not found"))

student["age"] = 22
student["city"] = "Lahore"
print(student)

del student["city"]
popped = student.pop("marks")
print("removed:", popped)
print(student)

print("name" in student)
print(list(student.keys()))
print(list(student.values()))

for key, value in student.items():
    print(key, ":", value)
