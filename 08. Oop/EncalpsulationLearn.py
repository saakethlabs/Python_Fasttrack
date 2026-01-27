# * Encapsulation in programming, 
# particularly in Object-Oriented Programming (OOP), 
# * refers to the bundling of data (attributes) 
# and the methods (functions) that operate 
# on that data into a single unit, 
# typically a class

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # private attribute

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds!")

    def get_balance(self):
        return self.__balance
    

ba = BankAccount("SaakethLabs", 1000)
print(ba.__balance)
print(ba.get_balance())