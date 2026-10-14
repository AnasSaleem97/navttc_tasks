# Task 16 - List Data Type
# Reference: https://www.programiz.com/python-programming/list

skills = ["Python", "SQL", "Machine Learning"]
skills.append("Deep Learning")
skills.insert(1, "Git")
print("Skills:", skills)

print("First skill:", skills[0])
print("Last two skills:", skills[-2:])

skills.remove("SQL")
popped_item = skills.pop()
print("Removed:", popped_item)
print("Remaining skills for Abubakar:", skills)

scores = [88, 72, 95, 60, 85]
scores.sort()
print("Sorted scores:", scores)
print("Total tests:", len(scores))
print("Max score:", max(scores))
print("Min score:", min(scores))
