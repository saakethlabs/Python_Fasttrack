# Creating a set
empty_set = set()
type(empty_set)
fruits = {"apple", "banana", "cherry"}
print(fruits)  # order is not guaranteed

nums = {1, 2, 2, 3, 4}
print(nums)  # {1, 2, 3, 4} — duplicates removed

# Creating a set from an iterable (like list, tuple, string)
numbers = set([1, 2, 3, 3, 2])
chars = set("hello")
# ? Detect Duplicate Ticket Holders

# * Sets Manipulation
A = {1, 2, 3}

# Add one element
A.add(4)
print(A)

# Add multiple elements
A.update([5, 6])
print(A)

# Remove elements
A.remove(2)   # Raises KeyError if not found
A.discard(10) # No error if not found
print(A)

# Pop removes and returns an arbitrary element
removed = A.pop()
print("Popped:", removed)
print(A)

# Clear all elements
A.clear()
print(A)

# * Set operations (Mathematical)

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Union
print(A | B)            # {1,2,3,4,5,6}
print(A.union(B))
# ? Find Countries in Either of Two Continents (Union)

# Intersection
print(A & B)            # {3,4}
print(A.intersection(B))
# ? Find Students Enrolled in Multiple Courses

# Difference
print(A - B)            # {1,2}
print(A.difference(B))
# ? Find Employees Who Left the Company 

# Symmetric Difference
print(A ^ B)            # {1,2,5,6}
print(A.symmetric_difference(B))
# ? Find Exclusive Offers Between Two Companies

fs = frozenset([1, 2, 3, 3, 2])
print(fs)

# fs.add(4)  # ❌ Error — frozensets are immutable
print(2 in fs)
