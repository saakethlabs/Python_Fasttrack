# Empty tuple
t1 = ()

# Tuple with elements
t2 = (1, 2, 3, 4)

# Tuple with mixed datatypes
t3 = (1, "Python", 3.14, True)

# Tuple with nested elements
t4 = (1, (2, 3), [4, 5])

# Tuple without parentheses (tuple packing)
t5 = 1, 2, 3

# Tuple unpacking
a, b, c = t5
print(a, b, c)


# Tuples are ordered
t = (10, 20, 30, 40)
print(t[0])     # Access by index
print(t[-1])    # Negative indexing

# Tuples are immutable
# t[1] = 100   # ❌ TypeError: 'tuple' object does not support item assignment

# Tuples can contain duplicate elements
t_dup = (1, 2, 2, 3)
print(t_dup)

# Concatenation
print(t1 + t2)

# Repetition
print(t1 * 2)

# Membership
print(2 in t1)
print(9 not in t2)

t = (1, 2, 2, 3, 4)

# count(value) → returns how many times a value occurs
print(t.count(2))   # Output: 2

# index(value, start, end) → returns the first index of the value
print(t.index(3))   # Output: 3

t = (5, 1, 3, 9, 2)

print(len(t))     # Length of tuple
print(max(t))     # Maximum value
print(min(t))     # Minimum value
print(sum(t))     # Sum of values
print(sorted(t))  # Returns a sorted list

t = (1, 2, 3)
l = list(t)  # Tuple → List
print(l)

l.append(4)
t = tuple(l)  # List → Tuple
print(t)

person = ("Alice", 25, "Engineer")

# Unpacking
name, age, profession = person
print(f"Name: {name}, Age: {age}, Profession: {profession}")