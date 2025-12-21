# Example 1: Basic error handling
try:
    number = int(input("Enter a number: "))
    print(f"You entered {number}")
except ValueError:
    print("Oops! That wasn't a valid number.")

# Example 2: Handling multiple exceptions
try:
    numerator = int(input("Enter numerator: "))
    print("Numerator recieved")
    denominator = int(input("Enter denominator: "))
    print("Denominator recieved")
    result = numerator / denominator
    print("Computed results")
    print(f"Result: {result}")
except ValueError:
    print("Please enter valid integers.")
except ZeroDivisionError:
    print("Denominator cannot be zero!")

# Example 3: Catch-all (use sparingly)
try:
    result = 10 / int(input("Enter a number: "))
    print(f"Result: {result}")
except Exception as e:
    print(f"An error occurred: {e}")

# Example 4: Using finally
try:
    f = open("example.txt", "r")
    print("File opened")
    content = f.read()
    print("File read")
    print(content)
except FileNotFoundError:
    print("File not found!")
finally:
    print("Closing file (if it was opened).")
    try:
        f.close()
    except:
        pass


# Example 5: Using else
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid input.")
else:
    print(f"Success! You entered {number}")


# Example 6: Raise your own exception
def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient funds!")
    return balance - amount

try:
    new_balance = withdraw(100, 150)
except ValueError as e:
    print("Error:", e)