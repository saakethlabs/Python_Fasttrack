# Loop through a list of fruits
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(f"I like {fruit}")


# Print numbers from 0 to 4
for i in range(5):
    print(i)

# Loop through each character in a string
for letter in "Python":
    print(letter)

# Loop through a dictionary
student = {"name": "Alice", "age": 20, "grade": "A"}

for key, value in student.items():
    print(f"{key}: {value}")


# Print numbers from 1 to 5
count = 1
while count <= 5:
    print(count)
    count += 1


# Print all combinations of numbers
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")

# Break example
for number in range(10):
    if number == 5:
        break  # Stop the loop
    print(number)

# Continue example
for number in range(10):
    if number % 2 == 0:
        continue  # Skip even numbers
    print(number)
