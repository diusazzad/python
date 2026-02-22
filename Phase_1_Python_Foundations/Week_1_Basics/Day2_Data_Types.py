"""
Day 2: Data Types
==================
PHP → Python

REFRESH (5 min):
- PHP: int, float, string, bool, array, object, null
- Python: int, float, str, bool, list, dict, tuple, set, None
- Python uses TitleCase for True, False, None
"""

# ============================================
# PART 1: NUMERIC TYPES
# ============================================

# Integer (no decimal)
count = 10
temperature = -20
population = 7_900_000_000  # Underscores allowed in Python 3.6+

print(f"Integer: {count}, Temperature: {temperature}")
print(f"Population: {population:,}")  # 7,900,000,000

# Float (decimal)
price = 19.99
pi = 3.14159
scientific = 1.5e10  # 15000000000.0

print(f"Price: {price}")
print(f"PI: {pi:.2f}")
print(f"Scientific: {scientific}")

# ============================================
# PART 2: STRING TYPE
# ============================================

# Single or double quotes (both same)
name = 'John'
name2 = "John"

# Multi-line strings
message = """
This is a
multi-line
string
"""
print(message)

# Raw strings (no escape processing)
path = r"C:\Users\John\Documents"
print(path)

# ============================================
# PART 3: BOOLEAN TYPE
# ============================================

# PHP: true/false → Python: True/False
is_active = True
is_deleted = False

# Operations return booleans
print(10 > 5)     # True
print(10 == 10)   # True
print(10 != 5)   # True

# ============================================
# PART 4: NONE TYPE (Like PHP null)
# ============================================

# PHP: null → Python: None
result = None
print(result is None)  # True

# Check if not None
if result is not None:
    print(result)
else:
    print("No result")

# ============================================
# PART 5: TYPE CONVERSION (CASTING)
# ============================================

# PHP: (int)$var → Python: int(var)

# String to int
num_str = "42"
num_int = int(num_str)
print(type(num_int))  # <class 'int'>

# String to float
price_str = "19.99"
price_float = float(price_str)
print(type(price_float))  # <class 'float'>

# Int to string
age = 25
age_str = str(age)
print(type(age_str))  # <class 'str'>

# Float to int (truncates decimal)
pi = 3.99
pi_int = int(pi)  # 3, not 4!
print(pi_int)

# ============================================
# PART 6: CHECKING TYPES
# ============================================

value = 42

# Type check
print(type(value) == int)        # True
print(isinstance(value, int))    # True
print(isinstance(value, (int, float)))  # True (int OR float)

# ============================================
# PRACTICE EXERCISES
# ============================================

# Exercise 1: Convert string "123" to int, add 77, print result
# YOUR CODE HERE:
num = int("123") + 77
print(f"Result: {num}")  # 200


# Exercise 2: Convert float 99.9 to int, multiply by 10, print
# YOUR CODE HERE:
val = int(99.9) * 10
print(f"Result: {val}")  # 990


# Exercise 3: Create variables of each type, print type of each
# YOUR CODE HERE:
my_int = 10
my_float = 10.5
my_str = "hello"
my_bool = True
my_none = None

print(type(my_int))
print(type(my_float))
print(type(my_str))
print(type(my_bool))
print(type(my_none))


# Exercise 4: User inputs string "45.5", convert to float, add 10
# Simulating input (in real code use input())
num_str = "45.5"
num_float = float(num_str) + 10
print(f"Result: {num_float}")  # 55.5


# ============================================
# RETENTION CHECK
# ============================================

# 1. What's Python's equivalent of PHP null?
# Answer: None

# 2. How do you convert "100" to integer?
# Answer: int("100")

# 3. What happens when you convert 7.9 to int?
# Answer: 7 (truncates, doesn't round)

# 4. True or False: Python uses true/false?
# Answer: False - uses True/False

# 5. How to check if variable is None?
# Answer: result is None
