"""
Day 7: Input & Casting
======================
PHP input() → Python input()

REFRESH:
- PHP: $var = trim(fgets(STDIN));
- Python: var = input()
- Always returns string in Python!
"""

# ============================================
# PART 1: BASIC INPUT
# ============================================

# In Python, input() pauses and waits for user
# NOTE: In Jupyter/ notebooks, use: input("Enter name: ")
# This won't work in this script - showing for learning

# name = input("Enter your name: ")
# print(f"Hello, {name}")

# For demonstration (commented out):
# name = "Demo User"  # Simulating input
# print(f"Hello, {name}")

print("=== Input Demo (commented - runs in terminal) ===")
# Uncomment below to test in terminal:
# name = input("Enter your name: ")
# age = input("Enter your age: ")
# print(f"You are {name}, {age} years old")

# ============================================
# PART 2: TYPE CONVERSION (CASTING)
# ============================================

# input() ALWAYS returns string!
# You must convert manually

# String to Integer
num_str = "42"
num_int = int(num_str)
print(f"String to int: {num_int}, type: {type(num_int)}")

# String to Float
price_str = "19.99"
price_float = float(price_str)
print(f"String to float: {price_float}, type: {type(price_float)}")

# Integer to String
age = 25
age_str = str(age)
print(f"Int to string: {age_str}, type: {type(age_str)}")

# Float to Integer (pitruncates!)
 = 3.99
pi_int = int(pi)
print(f"Float to int: {pi_int}")  # 3, not 4!

# Integer to Float (automatic!)
num = 42
num_float = float(num)
print(f"Int to float: {num_float}")  # 42.0

# ============================================
# PART 3: SAFE INPUT (HANDLING ERRORS)
# ============================================

# Basic input with default
def get_int(prompt="Enter number: "):
    """Get integer from user with error handling"""
    while True:
        try:
            value = input(prompt)
            return int(value)
        except ValueError:
            print("Please enter a valid integer!")

def get_float(prompt="Enter decimal: "):
    """Get float from user with error handling"""
    while True:
        try:
            value = input(prompt)
            return float(value)
        except ValueError:
            print("Please enter a valid number!")

# Demo with hardcoded values (replace with input() in terminal)
# Example usage (uncomment to test):
# age = get_int("Enter your age: ")
# price = get_float("Enter price: ")

print("Functions created: get_int(), get_float()")
print("Use these in terminal with: get_int() or get_float()")

# ============================================
# PART 4: COMMAND LINE ARGUMENTS
# ============================================

# PHP: $argv in CLI
# Python: sys.argv

# import sys
# if len(sys.argv) > 1:
#     print(f"First arg: {sys.argv[1]}")

# Demo:
import sys
print(f"Script name: {sys.argv[0]}")
print("Args passed: (none in this run)")

# ============================================
# PRACTICE EXERCISES
# ============================================

# Exercise 1: Convert "123" to int, add 77
# YOUR CODE HERE:
result = int("123") + 77
print(f"Result: {result}")  # 200


# Exercise 2: Get number from user, double it (use input())
# Simulating: uncomment in terminal
# num = float(input("Enter number: "))
# print(f"Double: {num * 2}")

# For testing without input():
num = 10  # Simulating user input
doubled = num * 2
print(f"Double of {num}: {doubled}")


# Exercise 3: Ask user for name and age, print "Name is Age years old"
# YOUR CODE HERE (simulating):
name = "John"  # Replace with input()
age = 30       # Replace with input()
print(f"{name} is {age} years old")


# Exercise 4: Convert "9.5" to int - what happens?
# YOUR CODE HERE:
result = int(9.5)  # Truncates!
print(f"int(9.5) = {result}")  # 9


# Exercise 5: Create calculator that adds two inputs
# YOUR CODE HERE (simulating):
a = 10  # Replace with float(input())
b = 20  # Replace with float(input())
print(f"{a} + {b} = {a + b}")


# ============================================
# REAL INPUT EXAMPLES (Run in Terminal)
# ============================================

print("\n=== Real Input Examples (Run in Terminal) ===")
print("Example 1: Simple name input")
print('# name = input("Enter name: ")')
print('# print(f"Hello {name}")')

print("\nExample 2: Calculator")
print('# a = float(input("First number: "))')
print('# b = float(input("Second number: "))')
print('# print(f"Sum: {a + b}")')

print("\nExample 3: Multiple values")
print('# x, y = input("Enter two values: ").split()')
print('# print(f"Values: {x}, {y}")')


# ============================================
# RETENTION CHECK
# ============================================

# 1. What does input() always return?
# Answer: String

# 2. How to convert string "42" to int?
# Answer: int("42")

# 3. What happens converting 9.7 to int?
# Answer: 9 (truncates, doesn't round)

# 4. How to safely get integer from user?
# Answer: Use try/except with int(input())

# 5. What is sys.argv[0]?
# Answer: The script name itself
