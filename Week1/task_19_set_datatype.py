# Task 19 - Set Data Type
# Reference: https://www.programiz.com/python-programming/set

my_skills = {"Python", "SQL", "Git"}
needed_skills = {"Python", "TensorFlow", "Docker"}

my_skills.add("Pandas")
my_skills.discard("Git")
print("Abubakar's skills:", my_skills)

common = my_skills.intersection(needed_skills)
all_skills = my_skills.union(needed_skills)
to_learn = needed_skills.difference(my_skills)

print("Common skills:", common)
print("Combined skills:", all_skills)
print("Skills to learn:", to_learn)

raw_list = [1, 2, 2, 3, 4, 4, 5]
unique_set = set(raw_list)
print("Removed duplicates:", unique_set)
