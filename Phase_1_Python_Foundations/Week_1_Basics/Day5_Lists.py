"""
Day 5: Lists Basics
===================
PHP Array → Python List

REFRESH:
- PHP: $arr = [1, 2, 3] or array(1, 2, 3)
- Python: arr = [1, 2, 3]
- PHP arrays are ordered dictionaries, Python lists are true arrays
"""

# ============================================
# PART 1: CREATING LISTS
# ============================================

# Empty list
empty = []
empty2 = list()

# With values
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]
mixed = [1, "hello", 3.14, True]

# List from string (like PHP str_split())
text = "hello"
chars = list(text)
print(chars)  # ['h', 'e', 'l', 'l', 'o']

# ============================================
# PART 2: ACCESSING ELEMENTS
# ============================================

fruits = ["apple", "banana", "cherry", "date"]

# By index (0-based, like PHP)
print(fruits[0])   # apple
print(fruits[1])   # banana
print(fruits[-1])  # cherry (last item)
print(fruits[-2])  # banana (second to last)

# ============================================
# PART 3: SLICING LISTS
# ============================================

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numbers[2:5])   # [2, 3, 4] (index 2 to 4)
print(numbers[:5])    # [0, 1, 2, 3, 4] (start to 4)
print(numbers[5:])    # [5, 6, 7, 8, 9] (5 to end)
print(numbers[::2])  # [0, 2, 4, 6, 8] (every 2nd)
print(numbers[::-1]) # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] (reverse)

# ============================================
# PART 4: CHECKING LENGTH
# ============================================

fruits = ["apple", "banana", "cherry"]

# PHP: count($fruits)
# Python: len(fruits)
print(len(fruits))  # 3

# Empty check
if fruits:
    print("Not empty")

if not fruits:
    print("Empty")

# ============================================
# PART 5: CHECKING MEMBERSHIP
# ============================================

fruits = ["apple", "banana", "cherry"]

# PHP: in_array("apple", $fruits)
# Python: "apple" in fruits
print("apple" in fruits)    # True
print("grape" in fruits)    # False
print("banana" not in fruits)  # False

# ============================================
# PART 6: NESTED LISTS
# ============================================

# 2D list (like PHP 2D array)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0])      # [1, 2, 3]
print(matrix[0][0])  # 1
print(matrix[1][2])  # 6

# ============================================
# PART 7: LIST UNPACKING (Like PHP list())
# ============================================

# PHP: list($a, $b, $c) = [1, 2, 3];
# Python:
a, b, c = [1, 2, 3]
print(a, b, c)  # 1 2 3

# With starred expression (rest)
first, *rest = [1, 2, 3, 4, 5]
print(first)  # 1
print(rest)    # [2, 3, 4, 5]

# Swap values
x, y = 1, 2
x, y = y, x
print(x, y)  # 2 1

# ============================================
# PRACTICE EXERCISES
# ============================================

# Exercise 1: Create list of 5 fruits, print first and last
# YOUR CODE HERE:
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(fruits[0], fruits[-1])  # apple elderberry


# Exercise 2: Get elements at index 1, 2, 3 from [0,1,2,3,4,5]
# YOUR CODE HERE:
nums = [0, 1, 2, 3, 4, 5]
print(nums[1:4])  # [1, 2, 3]


# Exercise 3: Reverse list [1,2,3,4,5] using slicing
# YOUR CODE HERE:
nums = [1, 2, 3, 4, 5]
print(nums[::-1])  # [5, 4, 3, 2, 1]


# Exercise 4: Check if "cat" is in ["dog", "cat", "bird"]
# YOUR CODE HERE:
pets = ["dog", "cat", "bird"]
print("cat" in pets)  # True


# Exercise 5: Unpack [10, 20, 30] into a, b, c
# YOUR CODE HERE:
a, b, c = [10, 20, 30]
print(a, b, c)  # 10 20 30


# Exercise 6: Create 3x3 matrix, access center element
# YOUR CODE HERE:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[1][1])  # 5


# ============================================
# RETENTION CHECK
# ============================================

# 1. How to access first element of list?
# Answer: list[0]

# 2. How to get last element?
# Answer: list[-1]

# 3. How to get elements 2 to 5 (exclusive)?
# Answer: list[2:5]

# 4. How to reverse a list?
# Answer: list[::-1]

# 5. How to check if item exists in list?
# Answer: item in list
