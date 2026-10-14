# Task 18 - String Data Type
# Reference: https://www.programiz.com/python-programming/string

text = "  hello, my name is Abubakar  "
cleaned = text.strip()

print("Original:", text)
print("Stripped:", cleaned)
print("Uppercase:", cleaned.upper())
print("Title Case:", cleaned.title())
print("Replaced:", cleaned.replace("Abubakar", "Abubakar Siddique"))

words = cleaned.split()
print("Word list:", words)
print("Joined:", "-".join(words))

print("Starts with 'hello':", cleaned.startswith("hello"))
print("Find 'name':", cleaned.find("name"))
print("First 5 chars:", cleaned[:5])
print("Reversed:", cleaned[::-1])
