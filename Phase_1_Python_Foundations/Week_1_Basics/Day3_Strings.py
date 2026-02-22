"""
Day 3: Strings
===============
PHP → Python

REFRESH:
- PHP: "Hello $name" or 'Hello ' . $name
- Python: f"Hello {name}" or "Hello " + name
"""

# ============================================
# PART 1: CREATING STRINGS
# ============================================

# Single quotes
first = 'Hello'

# Double quotes
second = "Hello"

# Multi-line (triple quotes)
message = """
This is
a multi-line
string
"""

# Raw string (for paths)
path = r"C:\Users\Admin\Documents"

# ============================================
# PART 2: F-STRINGS (FORMATTED STRINGS) - IMPORTANT!
# ============================================

name = "John"
age = 30

# PHP: "Name: $name, Age: $age"
# Python:
print(f"Name: {name}, Age: {age}")

# Expressions inside f-strings
print(f"Age in 10 years: {age + 10}")
print(f"Double age: {age * 2}")

# Format specifiers
price = 19.999
print(f"Price: {price:.2f}")   # Price: 20.00
print(f"Price: {price:.0f}")   # Price: 20

number = 42
print(f"Number: {number:05d}")  # Number: 00042

# ============================================
# PART 3: STRING CONCATENATION
# ============================================

# Using + (like PHP .)
greeting = "Hello" + " " + "World"
print(greeting)  # Hello World

# Using join()
words = ["Hello", "World"]
result = " ".join(words)
print(result)  # Hello World

# Using * to repeat
repeat = "Ha" * 3
print(repeat)  # HaHaHa

# ============================================
# PART 4: STRING SLICING
# ============================================

text = "Hello World"

# Get character by index (0-based)
print(text[0])   # H
print(text[1])   # e
print(text[-1])  # d (last character)

# Slicing [start:end] (end is exclusive!)
print(text[0:5])    # Hello (characters 0-4)
print(text[6:])     # World (6 to end)
print(text[:5])     # Hello (start to 4)
print(text[::2])   # HloWrd (every 2nd char)
print(text[::-1])  # dlroW olleH (reverse!)

# ============================================
# PART 5: STRING LENGTH
# ============================================

text = "Hello"

# PHP: strlen($text)
# Python: len(text)
print(len(text))  # 5

# Empty check
if text:
    print("Not empty")

if not text:
    print("Empty")

# ============================================
# PART 6: ESCAPE SEQUENCES
# ============================================

# Newline
print("Line 1\nLine 2")

# Tab
print("Col1\tCol2")

# Single quote in single-quoted string
print('It\'s a dog')

# Double quote in double-quoted string
print("She said \"Hello\"")

# Raw string for paths
path = r"C:\Users\Admin\Documents\note.txt"
print(path)  # C:\Users\Admin\Documents\note.txt

# ============================================
# PRACTICE EXERCISES
# ============================================

# Exercise 1: Create variables for first name and last name
# Concatenate them with a space, print result
# YOUR CODE HERE:
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)  # John Doe


# Exercise 2: Use f-string to print: "Product: Laptop, Price: $999.99"
# YOUR CODE HERE:
product = "Laptop"
price = 999.99
print(f"Product: {product}, Price: ${price}")


# Exercise 3: Extract "World" from "Hello World" using slicing
# YOUR CODE HERE:
text = "Hello World"
print(text[6:])  # World


# Exercise 4: Reverse the string "Python"
# YOUR CODE HERE:
text = "Python"
print(text[::-1])  # nohtyP


# Exercise 5: Format number 42 with leading zeros (00042)
# YOUR CODE HERE:
num = 42
print(f"{num:05d}")  # 00042


# ============================================
# RETENTION CHECK
# ============================================

# 1. How do you get character at index 3 of string "Hello"?
# Answer: text[3] → 'l'

# 2. How to get "Hel" from "Hello World"?
# Answer: text[0:3] or text[:3]

# 3. How to reverse a string?
# Answer: text[::-1]

# 4. What does f-string stand for?
# Answer: formatted string literal

# 5. How to get string length in Python?
# Answer: len(text)
