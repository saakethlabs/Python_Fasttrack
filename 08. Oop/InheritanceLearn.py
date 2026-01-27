# * Inheritance
# * Inheritance in Python is a fundamental concept in object-oriented programming (OOP) that allows a new class (child class or subclass)
# *  to inherit attributes and methods from an existing class (parent class, superclass, or base class).

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Some generic sound")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} says: Meow!")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} says: Woof!")


cat = Cat("Whiskers")
cat.speak()








class Vehicle:
    def start(self):
        print("Vehicle started")

class Car(Vehicle):
    pass

car = Car()
car.start()
