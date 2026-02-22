"""
Day 1: Hello World & Variables
==============================
PHP Developer → Python

REFRESH (5 min):
- Python uses indentation for code blocks (no {} or endif)
- No $ prefix for variables
- print() is like echo
"""

# ============================================
# PART 1: HELLO WORLD
# ============================================

# PHP: echo "Hello World";
# Python:
print("Hello World")

# Multiple print statements
print("Hello")
print("World")

# Print without newline
print("Hello", end=" ")
print("World")

# ============================================
# PART 2: VARIABLES
# ============================================

# PHP: $name = "John";
name = "John"

# PHP: $age = 25;
age = 25

# PHP: $price = 19.99;
price = 19.99

# PHP: $is_active = true;
is_active = True

# Multiple assignment
x, y, z = 1, 2, 3

# Same value to multiple variables
a = b = c = 0

# ============================================
# PART 3: PRINTING VARIABLES
# ============================================

# PHP: echo "Name: $name";
# Python (f-strings - IMPORTANT!):
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Price: {price}")
print(f"Active: {is_active}")

# Multiple variables in one print
print(f"Name: {name}, Age: {age}, Active: {is_active}")

# ============================================
# PART 4: GETTING VARIABLE INFO
# ============================================

# PHP: gettype($name);
# Python:
print(type(name))    # <class 'str'>
print(type(age))     # <class 'int'>
print(type(price))   # <class 'float'>
print(type(is_active))  # <class 'bool'>

# Check type (PHP: is_string($name))
print(isinstance(name, str))   # True
print(isinstance(age, int))    # True

# ============================================
# PRACTICE EXERCISES
# ============================================

# Exercise 1: Create variables for a person
# Name: "Alice", Age: 30, Salary: 50000.50, Is Employed: True
# Print all using f-string

# YOUR CODE HERE:
person_name = "Alice"
person_age = 30
person_salary = 50000.50
person_employed = True

print(f"Name: {person_name}")
print(f"Age: {person_age}")
print(f"Salary: {person_salary}")
print(f"Employed: {person_employed}")


# Exercise 2: Create variables for a product
# Product name, price, in_stock (boolean)
# Print: "Product: X, Price: $Y, In Stock: Yes/No"

# YOUR CODE HERE:
product_name = "Laptop"
product_price = 999.99
product_in_stock = True

stock_text = "Yes" if product_in_stock else "No"
print(f"Product: {product_name}, Price: ${product_price}, In Stock: {stock_text}")


# Exercise 3: Calculate total price
# price = 100, tax = 20, quantity = 3
# Print: "Total: $X"

# YOUR CODE HERE:
item_price = 100
tax = 20
quantity = 3
total = (item_price + tax) * quantity
print(f"Total: ${total}")


# ============================================
# BONUS: Print formatting
# ============================================

# Round numbers
price = 19.999
print(f"Price: {price:.2f}")  # Price: 20.00

# Pad numbers with zeros
num = 7
print(f"Number: {num:03d}")   # Number: 007

# ============================================
# RETENTION CHECK (Try from memory!)
# ============================================

# 1. Create variable `city = "Tokyo"` and print it
# 2. Create variables for a book: title, author, pages, is_bestseller
# 3. Print: "The book 'X' by Y has Z pages"
# 4. Check type of a float variable
