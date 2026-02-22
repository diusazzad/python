"""
Day 6: List Operations
======================
PHP Array Functions → Python List Methods

REFRESH:
- PHP: array_push(), array_pop(), array_shift(), unset()
- Python: .append(), .pop(), .remove(), del
"""

# ============================================
# PART 1: ADDING ELEMENTS
# ============================================

fruits = ["apple", "banana"]

# Add to end (like PHP array_push())
fruits.append("cherry")
print(fruits)  # ['apple', 'banana', 'cherry']

# Add multiple items (like PHP array_merge())
fruits.extend(["date", "elderberry"])
print(fruits)  # ['apple', 'banana', 'cherry', 'date', 'elderberry']

# Insert at index (like PHP array_insert not native)
fruits.insert(1, "blueberry")
print(fruits)  # ['apple', 'blueberry', 'banana', 'cherry', 'date', 'elderberry']

# Concatenate lists (+)
list1 = [1, 2]
list2 = [3, 4]
combined = list1 + list2
print(combined)  # [1, 2, 3, 4]

# ============================================
# PART 2: REMOVING ELEMENTS
# ============================================

fruits = ["apple", "banana", "cherry", "banana"]

# Remove and return last item (like PHP array_pop())
last = fruits.pop()
print(last)   # cherry
print(fruits) # ['apple', 'banana', 'banana']

# Remove at specific index (like PHP unset($arr[1]))
fruits = ["apple", "banana", "cherry"]
removed = fruits.pop(1)  # Remove index 1
print(removed)  # banana
print(fruits)   # ['apple', 'cherry']

# Remove by value (like PHP array_diff but modifies in place)
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits)  # ['apple', 'cherry']

# Clear entire list
fruits.clear()
print(fruits)  # []

# Using del (like PHP unset())
fruits = ["apple", "banana", "cherry"]
del fruits[0]
print(fruits)  # ['banana', 'cherry']

# del multiple
del fruits[0:2]
print(fruits)  # []

# ============================================
# PART 3: FINDING ELEMENTS
# ============================================

fruits = ["apple", "banana", "cherry", "banana"]

# Find index (like PHP array_search())
print(fruits.index("banana"))   # 1 (first occurrence)
print(fruits.index("cherry"))   # 2

# Count occurrences (like PHP array_count_values() then access)
print(fruits.count("banana"))   # 2
print(fruits.count("apple"))    # 1

# ============================================
# PART 4: SORTING
# ============================================

numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# Sort in place (like PHP sort())
numbers.sort()
print(numbers)  # [1, 1, 2, 3, 4, 5, 6, 9]

# Sort and create new list (like PHP asort() + copy)
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
sorted_nums = sorted(numbers)
print(numbers)      # [3, 1, 4, 1, 5, 9, 2, 6] (unchanged)
print(sorted_nums) # [1, 1, 2, 3, 4, 5, 6, 9]

# Reverse sort
numbers = [3, 1, 4, 1, 5]
numbers.sort(reverse=True)
print(numbers)  # [5, 4, 3, 1, 1]

# Sort strings
fruits = ["banana", "apple", "cherry"]
fruits.sort()
print(fruits)  # ['apple', 'banana', 'cherry']

# Case-insensitive sort
fruits = ["Banana", "apple", "Cherry"]
fruits.sort(key=str.lower)
print(fruits)  # ['apple', 'Banana', 'Cherry']

# ============================================
# PART 5: REVERSING
# ============================================

numbers = [1, 2, 3, 4, 5]

# Reverse in place
numbers.reverse()
print(numbers)  # [5, 4, 3, 2, 1]

# Reverse copy
numbers = [1, 2, 3, 4, 5]
reversed_nums = numbers[::-1]
print(reversed_nums)  # [5, 4, 3, 2, 1]

# Using reversed() (returns iterator)
for num in reversed(numbers):
    print(num)

# ============================================
# PART 6: LIST COMPREHENSION (IMPORTANT!)
# ============================================

# PHP: array_map(fn($x) => $x * 2, [1, 2, 3])
# Python:
numbers = [1, 2, 3]
doubled = [x * 2 for x in numbers]
print(doubled)  # [2, 4, 6]

# With condition (like PHP array_filter)
numbers = [1, 2, 3, 4, 5]
evens = [x for x in numbers if x % 2 == 0]
print(evens)  # [2, 4]

# Create list from string
text = "hello"
chars = [c for c in text]
print(chars)  # ['h', 'e', 'l', 'l', 'o']

# Nested comprehension
matrix = [[i*3+j for j in range(3)] for i in range(3)]
print(matrix)  # [[0,1,2], [3,4,5], [6,7,8]]

# ============================================
# PRACTICE EXERCISES
# ============================================

# Exercise 1: Add "orange" to end of ["apple", "banana"]
# YOUR CODE HERE:
fruits = ["apple", "banana"]
fruits.append("orange")
print(fruits)  # ['apple', 'banana', 'orange']


# Exercise 2: Remove "banana" from ["apple", "banana", "cherry"]
# YOUR CODE HERE:
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits)  # ['apple', 'cherry']


# Exercise 3: Sort [5, 2, 8, 1, 9] in descending order
# YOUR CODE HERE:
nums = [5, 2, 8, 1, 9]
nums.sort(reverse=True)
print(nums)  # [9, 8, 5, 2, 1]


# Exercise 4: Use list comprehension to get squares of [1,2,3,4,5]
# YOUR CODE HERE:
nums = [1, 2, 3, 4, 5]
squares = [x**2 for x in nums]
print(squares)  # [1, 4, 9, 16, 25]


# Exercise 5: Filter only names starting with 'A' from ["Alex", "Bob", "Alice", "Anna"]
# YOUR CODE HERE:
names = ["Alex", "Bob", "Alice", "Anna"]
a_names = [n for n in names if n.startswith("A")]
print(a_names)  # ['Alex', 'Alice', 'Anna']


# Exercise 6: Find index of "cherry" in ["apple", "banana", "cherry"]
# YOUR CODE HERE:
fruits = ["apple", "banana", "cherry"]
print(fruits.index("cherry"))  # 2


# ============================================
# RETENTION CHECK
# ============================================

# 1. How to add item to end of list?
# Answer: list.append(item)

# 2. How to remove item by value?
# Answer: list.remove(value)

# 3. How to sort list in place?
# Answer: list.sort()

# 4. What does list comprehension return?
# Answer: A new list

# 5. How to get last item and remove it?
# Answer: list.pop()
