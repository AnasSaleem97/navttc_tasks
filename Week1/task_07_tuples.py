# Task 07 - Tuples

student = ("Abubakar", 21, "Lahore", "Python")

print(student)
print(student[0])
print(student[-1])
print(student[1:3])

print(len(student))
print("Abubakar" in student)

nums = (3, 1, 4, 1, 5, 9, 1)
print(nums.count(1))
print(nums.index(4))

name, age, city, course = student
print(name, age, city, course)

t1 = (1, 2, 3)
t2 = (4, 5, 6)
print(t1 + t2)
print(t1 * 3)

as_list = list(student)
as_list.append("NAVTTC")
back = tuple(as_list)
print(back)
