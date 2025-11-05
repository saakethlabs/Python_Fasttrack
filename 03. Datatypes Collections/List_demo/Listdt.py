## Creating a list

# Empty list
empty_list = []

# List of integers
numbers = [1, 2, 3, 4]

# Mixed data types
mixed = [1, "two", 3.0, [4, 5]]

# Using list() constructor
from_string = list("hello")
print(from_string)  # ['h', 'e', 'l', 'l', 'o']


## Accessing List Elements

my_list = [10, 20, 30, 40, 50]

# Indexing
print(my_list[0])    # 10
print(my_list[-1])   # 50 (last item)
# ? Stock price movement

# Slicing
print(my_list[1:4])  # [20, 30, 40]
print(my_list[:3])   # [10, 20, 30]
print(my_list[::2])  # [10, 30, 50]
# ? # Orders received each day (2 weeks)
# ? orders = [120, 135, 150, 160, 180, 200, 220,  # Week 1
# ?         210, 205, 190, 230, 240, 260, 270]  # Week 2

## Modifying Lists

my_list = [10, 20, 30]

# Changing an element
my_list[1] = 99
print(my_list)  # [10, 99, 30]

# Adding new elements
my_list.append(40)
print(my_list)  # [10, 99, 30, 40]


## Append
lst = [1, 2]
lst.append(3)
print(lst)  # [1, 2, 3]
# ? At the start of the day, your inventory list is empty — you’ll append items as they arrive.


## Extend
lst = [1, 2]
lst.extend([3, 4])
print(lst)  # [1, 2, 3, 4]
# ? At the start of the day, your inventory list with existing list — you’ll append items as they arrive.


## Insert
lst = [1, 3]
lst.insert(1, 2)
print(lst)  # [1, 2, 3]




## Remove
lst = [1, 2, 2, 3]
lst.remove(2)
print(lst)  # [1, 2, 3]
# ? train_route = ["Mahalakshmi", "Isckon", "Sandal soap factory", "Peenya", "Peenya Industries"]
# ? Add a stop and remove a stop


## Pop
lst = [10, 20, 30]
print(lst.pop())   # 30
print(lst.pop(0))  # 10
print(lst)         # [20]


## Clear
lst = [1, 2, 3]
lst.clear()
print(lst)  # []


## index
lst = [10, 20, 30, 20]
print(lst.index(20))  # 1


## count
lst = [1, 2, 2, 3, 2]
print(lst.count(2))  # 3


## sort
nums = [3, 1, 4, 2]
nums.sort()
print(nums)  # [1, 2, 3, 4]

nums.sort(reverse=True)
print(nums)  # [4, 3, 2, 1]

# ? Sort list of prices from low to high and high to low


## reverse
lst = [1, 2, 3]
lst.reverse()
print(lst)  # [3, 2, 1]


## copy
a = [1, 2, 3]
b = a.copy()
b.append(4)
print(a)  # [1, 2, 3]
print(b)  # [1, 2, 3, 4]

# Other operations
a = [1, 2, 3]
b = [4, 5]

# Concatenation
print(a + b)  # [1, 2, 3, 4, 5]
# ? combine two different section students

# Repetition
print(a * 2)  # [1, 2, 3, 1, 2, 3]

# Membership
print(2 in a)   # True
print(9 not in a)  # True

# Length
print(len(a))  # 3
# ? Check if a student is in a class and print number of students in class

## min
# List of numbers
numbers = [5, 2, 9, 1, 7]

# Get the smallest number
smallest = min(numbers)
print("Minimum:", smallest)
# Output: Minimum: 1


## max
numbers = [5, 2, 9, 1, 7]

# Get the largest number
largest = max(numbers)
print("Maximum:", largest)
# Output: Maximum: 9


## sum
numbers = [5, 2, 9, 1, 7]

total = sum(numbers)
print("Sum:", total)
# Output: Sum: 24

# ? Get minimum, max marks scored by students