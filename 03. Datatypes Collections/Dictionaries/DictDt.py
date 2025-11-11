# Creating a simple dictionary
empty_dict = {}
student = {
    "name": "Alice",
    "age": 22,
    "major": "Computer Science"
}

print(student)

# Accessing values using keys
print(student["name"])      # Output: Alice
print(student["major"])     # Output: Computer Science

# Using get() avoids KeyError
print(student.get("age"))             # Output: 22
print(student.get("GPA", "N/A"))      # Default value if key is missing


# Adding a new key-value pair
student["GPA"] = 3.8

# Updating an existing key
student["age"] = 23

print(student)

# Removing a specific key
student.pop("GPA")

print(student)

print(student.keys())     # dict_keys(['name', 'age', 'major'])
print(student.values())   # dict_values(['Alice', 23, 'Computer Science'])
print(student.items())    # dict_items([('name', 'Alice'), ('age', 23), ...])

# Dictionary inside another dictionary
students = {
    "Alice": {"age": 22, "major": "CS"},
    "Bob": {"age": 24, "major": "Math"}
}

print(students["Alice"]["major"])  # Output: CS


grades = {"Alice": 85, "Bob": 90, "Charlie": 78}

print(len(grades))           # Number of items
print("Bob" in grades)       # Check if key exists
grades.clear()               # Remove all items
print(grades)