"""
Day 4: String Methods
=====================
PHP → Python

REFRESH:
- PHP: strtolower(), strtoupper(), strlen(), strpos()
- Python: .lower(), .upper(), .len(), .find() or .index()
"""

# ============================================
# PART 1: CASE CONVERSION
# ============================================

text = "Hello World"

# Lower/Upper
print(text.lower())   # hello world
print(text.upper())   # HELLO WORLD
print(text.capitalize())  # Hello world (first char)
print(text.title())   # Hello World (each word)

# Swap case
print(text.swapcase())  # hELLO wORLD

# ============================================
# PART 2: SEARCHING & FINDING
# ============================================

text = "Hello World"

# Find position (like PHP strpos())
# Returns index or -1 if not found
print(text.find("World"))    # 6
print(text.find("Python"))   # -1

# index() is similar but raises error if not found
try:
    print(text.index("World"))  # 6
except ValueError:
    print("Not found")

# Check if substring exists (like PHP strpos() !== false)
if "World" in text:
    print("Found!")

if "Python" not in text:
    print("Not found!")

# Count occurrences
print(text.count("l"))  # 3

# ============================================
# PART 3: REPLACING
# ============================================

text = "Hello World"

# Replace (like PHP str_replace())
new_text = text.replace("World", "Python")
print(new_text)  # Hello Python

# Replace all occurrences
text = "aaaabaaa"
print(text.replace("a", "x"))  # xxxxbaaa
print(text.replace("a", "x", 2))  # xxaabaaa (max 2 replacements)

# ============================================
# PART 4: SPLITTING & JOINING
# ============================================

# Split (like PHP explode())
text = "apple,banana,cherry"
fruits = text.split(",")
print(fruits)  # ['apple', 'banana', 'cherry']

# Split by whitespace
text = "Hello World"
print(text.split())  # ['Hello', 'World']

# Join (like PHP implode())
words = ["Hello", "World"]
result = " ".join(words)
print(result)  # Hello World

# Join with different separator
words = ["apple", "banana", "cherry"]
result = ", ".join(words)
print(result)  # apple, banana, cherry

# ============================================
# PART 5: STRIPPING WHITESPACE
# ============================================

text = "   Hello World   "

print(text.strip())   # Hello World (removes both ends)
print(text.lstrip())  # Hello World   (left only)
print(text.rstrip())  #    Hello World (right only)

# Remove specific characters
text = "---Hello---"
print(text.strip("-"))  # Hello
print(text.lstrip("-")) # Hello---

# ============================================
# PART 6: CHECKING STRING CONTENT
# ============================================

text = "Hello123"

print(text.isalpha())    # False (has numbers)
print(text.isdigit())    # False
print(text.isalnum())    # True (letters + numbers only)
print(text.isnumeric())  # False
print(text.isspace())    # False

text = "   "
print(text.isspace())    # True

text = "HELLO"
print(text.isupper())    # True
print(text.islower())    # False

# ============================================
# PART 7: PADDING & ALIGNMENT
# ============================================

text = "Hello"

# Pad to length
print(text.ljust(10))    # Hello     (left align)
print(text.rjust(10))    #     Hello (right align)
print(text.center(10))  #   Hello   (center)

# Pad with character
print(text.ljust(10, "-"))   # Hello-----
print(text.rjust(10, "0"))   # 00000Hello

# Zfill (pad with zeros)
print(text.zfill(10))   # 00000Hello

# ============================================
# PRACTICE EXERCISES
# ============================================

# Exercise 1: Convert "PYTHON" to lowercase, then capitalize
# YOUR CODE HERE:
text = "PYTHON"
print(text.lower().capitalize())  # Python


# Exercise 2: Find position of "lo" in "Hello World"
# YOUR CODE HERE:
text = "Hello World"
print(text.find("lo"))  # 3


# Exercise 3: Replace all spaces with dashes in "Hello World"
# YOUR CODE HERE:
text = "Hello World"
print(text.replace(" ", "-"))  # Hello-World


# Exercise 4: Split "one,two,three" by comma, then join with " | "
# YOUR CODE HERE:
text = "one,two,three"
parts = text.split(",")
print(" | ".join(parts))  # one | two | three


# Exercise 5: Check if "  hello  " (with spaces) contains only letters after stripping
# YOUR CODE HERE:
text = "  hello  "
cleaned = text.strip()
print(cleaned.isalpha())  # True


# Exercise 6: Pad "Hi" with zeros to make it 5 characters
# YOUR CODE HERE:
text = "Hi"
print(text.zfill(5))  # 000Hi


# ============================================
# RETENTION CHECK
# ============================================

# 1. What does .strip() do?
# Answer: Removes whitespace from both ends

# 2. How to replace "foo" with "bar" in string?
# Answer: text.replace("foo", "bar")

# 3. How to check if "abc" is in string?
# Answer: "abc" in text

# 4. What does .split() return?
# Answer: A list of strings

# 5. How to join list with "-" separator?
# Answer: "-".join(list)
