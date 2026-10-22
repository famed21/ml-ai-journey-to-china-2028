
"""
strings.py
==================================================
PHASE 1: PYTHON FUNDAMENTALS
Topic: Strings and Text Manipulation

Learning objectives:
1. Understand strings and string indexing.
2. Use slicing to extract text.
3. Apply string methods.
4. Format strings using f-strings.
5. Search, replace, split, and join text.
6. Validate and manipulate user input.
7. Apply strings to practical problems.

Run:
    python3 strings.py
==================================================
"""


# ==================================================
# LESSON 1: WHAT IS A STRING?
# ==================================================

print("\n" + "=" * 50)
print("LESSON 1: WHAT IS A STRING?")
print("=" * 50)

name = "Thabiso"
language = 'Python'
message = """Welcome to your Python learning journey!"""

print(name)
print(language)
print(message)

# A string is a sequence of characters.
# You can use single quotes, double quotes,
# or triple quotes for multiline strings.

print("Type:", type(name))


# ==================================================
# LESSON 2: STRING CONCATENATION
# ==================================================

print("\n" + "=" * 50)
print("LESSON 2: CONCATENATION")
print("=" * 50)

first_name = "Thabiso"
last_name = "Thelingoane"

full_name = first_name + " " + last_name

print("Full name:", full_name)

# The + operator joins strings.
# The space must be added explicitly.

greeting = "Hello " * 3
print(greeting)

# Multiplication repeats a string.


# ==================================================
# LESSON 3: STRING LENGTH
# ==================================================

print("\n" + "=" * 50)
print("LESSON 3: STRING LENGTH")
print("=" * 50)

text = "Machine Learning"

print("Text:", text)
print("Number of characters:", len(text))

# len() counts characters, including spaces.


# ==================================================
# LESSON 4: STRING INDEXING
# ==================================================

print("\n" + "=" * 50)
print("LESSON 4: STRING INDEXING")
print("=" * 50)

word = "PYTHON"

print("First character:", word[0])
print("Second character:", word[1])
print("Last character:", word[-1])
print("Second-last character:", word[-2])

# Indexing starts at 0.
#
# P  Y  T  H  O  N
# 0  1  2  3  4  5
# -6 -5 -4 -3 -2 -1

# Strings are immutable: individual characters
# cannot be changed directly.


# ==================================================
# LESSON 5: STRING SLICING
# ==================================================

print("\n" + "=" * 50)
print("LESSON 5: STRING SLICING")
print("=" * 50)

word = "PYTHON PROGRAMMING"

print("First three:", word[0:3])
print("First six:", word[:6])
print("From index 7:", word[7:])
print("Last six:", word[-6:])
print("Every second character:", word[::2])
print("Reversed:", word[::-1])

# Syntax: text[start:stop:step]
# The stop index is excluded.


# ==================================================
# LESSON 6: CHANGING LETTER CASE
# ==================================================

print("\n" + "=" * 50)
print("LESSON 6: STRING CASE METHODS")
print("=" * 50)

text = "Python Is Awesome"

print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Title case:", text.title())
print("Capitalize:", text.capitalize())
print("Swap case:", text.swapcase())

# These methods return new strings.
# They do not modify the original string.


# ==================================================
# LESSON 7: REMOVING WHITESPACE
# ==================================================

print("\n" + "=" * 50)
print("LESSON 7: STRIPPING WHITESPACE")
print("=" * 50)

username = "   thabiso   "

print("Original:", repr(username))
print("Strip both sides:", repr(username.strip()))
print("Left strip:", repr(username.lstrip()))
print("Right strip:", repr(username.rstrip()))

# strip() is useful for cleaning user input.
# repr() makes surrounding spaces visible.


# ==================================================
# LESSON 8: SEARCHING INSIDE STRINGS
# ==================================================

print("\n" + "=" * 50)
print("LESSON 8: SEARCHING STRINGS")
print("=" * 50)

sentence = "Python is powerful and Python is useful"

print("Find Python:", sentence.find("Python"))
print("Count Python:", sentence.count("Python"))
print("Starts with Python:", sentence.startswith("Python"))
print("Ends with useful:", sentence.endswith("useful"))
print("Contains powerful:", "powerful" in sentence)

# find() returns the first index or -1 if absent.
# count() counts non-overlapping occurrences.
# The 'in' operator checks whether text exists.


# ==================================================
# LESSON 9: REPLACING TEXT
# ==================================================

print("\n" + "=" * 50)
print("LESSON 9: REPLACING STRINGS")
print("=" * 50)

sentence = "I am learning Java"

updated_sentence = sentence.replace("Java", "Python")

print("Original:", sentence)
print("Updated:", updated_sentence)

# replace(old, new) returns a new string.
# The original variable remains unchanged.


# ==================================================
# LESSON 10: SPLIT AND JOIN
# ==================================================

print("\n" + "=" * 50)
print("LESSON 10: SPLIT AND JOIN")
print("=" * 50)

languages = "Python,Java,C++,JavaScript"

language_list = languages.split(",")

print("String:", languages)
print("List:", language_list)
print("First language:", language_list[0])

joined_text = " | ".join(language_list)

print("Joined text:", joined_text)

# split() converts a string into a list.
# join() combines strings using a separator.


# ==================================================
# LESSON 11: CHECKING STRING CONTENT
# ==================================================

print("\n" + "=" * 50)
print("LESSON 11: STRING VALIDATION")
print("=" * 50)

text = "Python123"

print("Only letters:", text.isalpha())
print("Only digits:", text.isdigit())
print("Letters and digits:", text.isalnum())
print("All lowercase:", text.islower())
print("All uppercase:", text.isupper())
print("Only whitespace:", text.isspace())

# These methods return True or False.
# Spaces and punctuation affect the results.


# ==================================================
# LESSON 12: F-STRINGS
# ==================================================

print("\n" + "=" * 50)
print("LESSON 12: STRING FORMATTING")
print("=" * 50)

name = "Thabiso"
age = 23
goal = "Master's in AI and Machine Learning"

print(f"My name is {name}.")
print(f"I am {age} years old.")
print(f"My goal is a {goal}.")

# f-strings insert variable values into text.

price = 19.5678
print(f"Price: {price:.2f}")

# :.2f displays a number to two decimal places.


# ==================================================
# LESSON 13: ESCAPE CHARACTERS
# ==================================================

print("\n" + "=" * 50)
print("LESSON 13: ESCAPE CHARACTERS")
print("=" * 50)

print("Hello\nWorld")
print("Python\tProgramming")
print("She said, \"Learn Python!\"")
print("C:\\Users\\Thabiso")

# \n creates a new line.
# \t creates a tab.
# \" inserts a quotation mark.
# \\ inserts a backslash.

# Raw strings preserve backslashes:
print(r"C:\Users\Thabiso\Documents")


# ==================================================
# LESSON 14: USER INPUT AND STRING CLEANING
# ==================================================

print("\n" + "=" * 50)
print("LESSON 14: CLEANING USER INPUT")
print("=" * 50)

user_name = input("Enter your name: ").strip()

if user_name:
    print(f"Welcome, {user_name.title()}!")
else:
    print("Error: Your name cannot be empty.")

# Strings are useful for accepting and validating
# information entered by users.


# ==================================================
# LESSON 15: STRING CONDITIONS
# ==================================================

print("\n" + "=" * 50)
print("LESSON 15: STRING DECISION-MAKING")
print("=" * 50)

command = input("Enter a command (start/stop/status): ")
command = command.strip().lower()

if command == "start":
    print("Starting the program...")
elif command == "stop":
    print("Stopping the program...")
elif command == "status":
    print("Program is running.")
else:
    print("Unknown command.")

# Combining strings with if/elif/else lets you
# build menus, command interpreters, and applications.


# ==================================================
# LESSON 16: PRACTICAL CYBERSECURITY EXAMPLE
# ==================================================

print("\n" + "=" * 50)
print("LESSON 16: BASIC LOG ANALYSIS")
print("=" * 50)

log_entry = (
    "2026-10-22 WARNING Failed login "
    "from 192.168.1.10"
)

print("Log:", log_entry)

if "WARNING" in log_entry:
    print("Warning event detected.")

if "Failed login" in log_entry:
    print("Possible authentication failure detected.")

# This is a simple text-matching demonstration.
# Real log analysis requires parsing, context,
# and additional validation.


# ==================================================
# PRACTICE CHALLENGES
# ==================================================

print("\n" + "=" * 50)
print("YOUR PRACTICE CHALLENGES")
print("=" * 50)

print("""
CHALLENGE 1: Name Formatter
Ask for a full name and display it in title case.

CHALLENGE 2: Palindrome Checker
Ask for a word and check whether it reads the
same forwards and backwards.
Hint: word == word[::-1]

CHALLENGE 3: Word Counter
Ask for a sentence and count its words.
Hint: len(sentence.split())

CHALLENGE 4: Character Counter
Ask for a sentence and count how many times
the letter 'a' occurs, ignoring case.

CHALLENGE 5: Username Validator
Require a username with 4-16 characters.
Allow only letters, numbers, and underscores.
Hint: isalnum() alone does not allow underscores.

CHALLENGE 6: Email Validator
Check whether an email contains '@' and a dot
after the '@'. Consider why this is not enough
to validate every real email address.

CHALLENGE 7: Log Scanner
Ask for a log entry and detect the words:
ERROR, WARNING, or INFO, ignoring case.

CHALLENGE 8: Text Analyzer
Ask for a paragraph and display:
- Total characters
- Total words
- Uppercase version
- Lowercase version
- Reversed text
""")

print("\nStrings lesson complete!")
print("Practise each challenge before moving on.")
