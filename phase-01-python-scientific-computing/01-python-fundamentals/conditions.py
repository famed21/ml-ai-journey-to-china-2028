
"""
conditions.py
================================================
PHASE 1: PYTHON FUNDAMENTALS
Topic: Conditional Logic and Decision-Making

Learning objectives:
1. Understand if, elif, and else.
2. Compare values using comparison operators.
3. Combine conditions using logical operators.
4. Use nested conditions.
5. Apply conditions to real-world problems.
6. Practise decision-making through exercises.

Run:
    python3 conditions.py
================================================
"""

# =================================================
# LESSON 1: THE BASIC IF STATEMENT
# =================================================

print("\n" + "=" * 50)
print("LESSON 1: THE IF STATEMENT")
print("=" * 50)

# A condition is an expression that evaluates to True or False.

age = 23

if age >= 18:
    print("You are an adult.")

# Explanation:
# - if checks whether a condition is True.
# - >= means greater than or equal to.
# - Indentation tells Python which code belongs to the if.


# =================================================
# LESSON 2: IF AND ELSE
# =================================================

print("\n" + "=" * 50)
print("LESSON 2: IF AND ELSE")
print("=" * 50)

age = 16

if age >= 18:
    print("You are allowed to enter.")
else:
    print("You are too young to enter.")

# The else block runs when the if condition is False.


# =================================================
# LESSON 3: IF, ELIF, AND ELSE
# =================================================

print("\n" + "=" * 50)
print("LESSON 3: IF, ELIF, AND ELSE")
print("=" * 50)

mark = 76

if mark >= 80:
    print("Grade: A")
elif mark >= 70:
    print("Grade: B")
elif mark >= 60:
    print("Grade: C")
elif mark >= 50:
    print("Grade: D")
else:
    print("Grade: F")

# elif means "else if".
# Python checks conditions from top to bottom.
# The first matching branch runs, and the rest are skipped.


# =================================================
# LESSON 4: COMPARISON OPERATORS
# =================================================

print("\n" + "=" * 50)
print("LESSON 4: COMPARISON OPERATORS")
print("=" * 50)

x = 10
y = 20

print("x == y:", x == y)  # Equal to
print("x != y:", x != y)  # Not equal to
print("x > y:", x > y)    # Greater than
print("x < y:", x < y)    # Less than
print("x >= y:", x >= y)  # Greater than or equal to
print("x <= y:", x <= y)  # Less than or equal to

# Remember:
# =  assigns a value.
# == compares two values.


# =================================================
# LESSON 5: LOGICAL OPERATORS
# =================================================

print("\n" + "=" * 50)
print("LESSON 5: LOGICAL OPERATORS")
print("=" * 50)

age = 23
has_id = True

# AND: both conditions must be True.
if age >= 18 and has_id:
    print("Access granted.")

# OR: at least one condition must be True.
is_student = True
has_discount_card = False

if is_student or has_discount_card:
    print("You qualify for a discount.")

# NOT: reverses a Boolean value.
is_blocked = False

if not is_blocked:
    print("Your account is active.")


# =================================================
# LESSON 6: USER INPUT
# =================================================

print("\n" + "=" * 50)
print("LESSON 6: USER INPUT")
print("=" * 50)

# input() returns a string.
# int() converts the input into an integer.

user_age = int(input("Enter your age: "))

if user_age < 0:
    print("Invalid age.")
elif user_age < 18:
    print("You are a minor.")
elif user_age < 60:
    print("You are an adult.")
else:
    print("You are a senior adult.")

# Try different ages to see how the output changes.


# =================================================
# LESSON 7: NESTED CONDITIONS
# =================================================

print("\n" + "=" * 50)
print("LESSON 7: NESTED CONDITIONS")
print("=" * 50)

username = input("Enter username: ")
password = input("Enter password: ")

# This is a learning example, not secure authentication.
if username == "admin":
    if password == "python123":
        print("Welcome, administrator!")
    else:
        print("Incorrect password.")
else:
    print("Unknown username.")

# A nested condition is an if statement inside another if.
# Never store real passwords directly in source code.


# =================================================
# LESSON 8: CONDITIONAL LOGIC IN MATHEMATICS
# =================================================

print("\n" + "=" * 50)
print("LESSON 8: MATHEMATICAL DECISION-MAKING")
print("=" * 50)

number = int(input("Enter an integer: "))

if number == 0:
    print("The number is zero.")
elif number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# % is the modulo operator.
# It returns the remainder after division.
# An even integer has a remainder of 0 when divided by 2.


# =================================================
# LESSON 9: CONDITIONS IN CYBERSECURITY
# =================================================

print("\n" + "=" * 50)
print("LESSON 9: CYBERSECURITY DECISIONS")
print("=" * 50)

failed_attempts = int(input("Failed login attempts: "))
account_locked = input("Is the account locked? (yes/no): ").lower()

if account_locked == "yes":
    print("ALERT: Account is locked.")
elif failed_attempts >= 5:
    print("WARNING: Investigate repeated failed logins.")
elif failed_attempts < 0:
    print("Invalid number of attempts.")
else:
    print("No lockout threshold reached.")

# This is a simplified educational example.
# Real security systems require additional safeguards.


# =================================================
# LESSON 10: CONDITIONAL EXPRESSIONS
# =================================================

print("\n" + "=" * 50)
print("LESSON 10: CONDITIONAL EXPRESSIONS")
print("=" * 50)

temperature = 30

weather = "Hot" if temperature >= 25 else "Cool"

print("The weather is:", weather)

# A conditional expression is a compact if/else.


# =================================================
# PRACTICE EXERCISES
# =================================================

print("\n" + "=" * 50)
print("YOUR PRACTICE CHALLENGES")
print("=" * 50)

print("""
EXERCISE 1:
Ask the user for a number.
Print whether it is positive, negative, or zero.

EXERCISE 2:
Ask for a mark between 0 and 100.
Reject invalid marks, then assign a grade.

EXERCISE 3:
Ask for a username and age.
Grant access only if the username is correct
AND the user is at least 18.

EXERCISE 4:
Ask for three numbers.
Use conditions to find the largest number.

EXERCISE 5:
Ask for a password length.
Classify it as short (less than 8 characters)
or long (8 characters or more).

EXERCISE 6:
Create a simple login-monitoring program.
Warn the user if failed attempts reach 5.
Reject negative attempt counts.
""")

print("\nLesson complete! Now solve the exercises yourself.")

