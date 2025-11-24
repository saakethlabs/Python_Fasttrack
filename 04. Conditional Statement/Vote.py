# Ask a user for their age and print whether they can vote or not.

age = int(input("Please enter your age: "))

if age > 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")