# Task 04 - String Operations

name = "Abubakar"

print(len(name))
print(name[0])
print(name[-1])
print(name[0:4])
print(name[::-1])

print(name.upper())
print(name.lower())
print(name.replace("Abubakar", "Ali"))

sentence = "  python is fun  "
print(sentence.strip())
print(sentence.strip().split())

words = ["python", "is", "great"]
print(" ".join(words))

print("Abu" in name)
print(name.startswith("Abu"))
print(name.endswith("kar"))
print(name.find("bak"))
print(name.count("a"))
