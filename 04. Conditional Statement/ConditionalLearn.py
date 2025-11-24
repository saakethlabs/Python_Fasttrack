temperature = 30

# If
if temperature > 25:
    print("It's a hot day!")

# If else

temperature = 20

if temperature > 25:
    print("It's a hot day!")
else:
    print("It's not too hot.")


# If elif and else
temperature = 15

if temperature > 30:
    print("It's really hot!")
elif temperature > 20:
    print("It's a warm day.")
elif temperature > 15:
    print("It's okay")
else:
    print("It's a bit cold.")


# Nested if statement
age = 18
has_ticket = True

if age >= 18:
    if has_ticket:
        print("You can enter the concert!")
    else:
        print("You need a ticket to enter.")
else:
    print("You are too young to enter.")


# and and or
age = 20
is_student = True

if age < 25 and is_student:
    print("You get a student discount!")

# True and True => ✅
# True and False => ❌
# False and True => ❌
# False and False => ❌

age = 50
is_veteran = True

if age > 65 or is_veteran:
    print("You qualify for a special discount!")

# True or True => ✅
# True or False => ✅
# False or True => ✅
# False or False => ❌


# not
is_raining = False

if not is_raining:
    print("You don’t need an umbrella!")


# ? Questions
# Ask a user for their age and print whether they can vote or not.
# Odd or Even
# Positive, Negative or Zero
# Vowel or consonants
# Pass or fail
marks = 50
if marks > 35:
    print("Passed")
else:
    print("Fail")
# Greatest of two numbers
# Age category
    # 0–12 → “Child”
    # 13–19 → “Teenager”
    # 20–59 → “Adult”
    # 60+ → “Senior”
# Multiple of 5
num = 25
if num %5 == 0:
    print("Multiple of 5")
else:
    print("Not a multiple of 5")