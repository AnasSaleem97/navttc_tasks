# Task 06 - Lists

fruits = ["mango", "apple", "banana", "orange"]

print(fruits)
print(fruits[0])
print(fruits[-1])
print(fruits[1:3])

fruits[1] = "kiwi"
fruits.append("grape")
fruits.insert(0, "strawberry")
print(fruits)

fruits.remove("banana")
fruits.pop()
print(fruits)

print(len(fruits))
print("mango" in fruits)

nums = [5, 2, 8, 1, 9]
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)

print(nums.count(5))
print(nums.index(8))
