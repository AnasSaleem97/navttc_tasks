# Task 20 - Dictionary Data Type
# Reference: https://www.programiz.com/python-programming/dictionary

profile = {
    "name": "Abubakar",
    "track": "Artificial Intelligence",
    "batch": 2026,
    "gpa": 3.7
}

print("Profile:", profile)
print("Student name:", profile["name"])
print("City (using get):", profile.get("city", "Not specified"))

profile["city"] = "Lahore"
profile["gpa"] = 3.8
print("Updated profile:", profile)

removed_item = profile.pop("batch")
print("Popped batch:", removed_item)

print("Keys:", list(profile.keys()))
print("Values:", list(profile.values()))

for k, v in profile.items():
    print(f"{k}: {v}")
