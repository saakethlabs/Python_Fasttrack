# Defn: Is a blueprint or template that groups attributes and functions into a single unit.

class Dog:

    name = ''
    breed = ''

    def __init__(self, name, breed):
        self.name = name      # instance variable
        self.breed = breed

    def bark(self):
        print(f"{self.name} says: Woof!")

class Student:

    name = ''
    age = ''
    roll_no = ''
    grade = ''

    def __init__(self, name, age, roll_no, grade):
        self.name = name
        self.age = age
        self.roll_no = roll_no
        self.grade = grade

    def add_grade(self, grade):
        self.grade = grade
    
    def print_grade(self):
        print(f"Grade of {self.name} is {self.grade}")

student1 = Student('SaakethLabs', 26, 15, 'A+')

print(student1.name)
print(student1.age)
print(student1.roll_no)
print(student1.grade)

student2 = Student("AnanthLabs", 18, 16, 'A')