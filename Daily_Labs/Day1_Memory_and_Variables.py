"""
DAILY LAB: DAY 1 - MEMORY AND VARIABLES
Topic: How Python "thinks" about Data.

VISUAL REPRESENTATION:
[ Variable Name ] ----> ( Memory Address ) ----> [ Value ]
     "x"          ---->   0x10293485     ---->     10

In AI, we deal with massive matrices. Understanding how variables 
point to data is crucial for performance!
"""

# CLEAN CODE: Use descriptive names
user_age = 25
high_score = 98.5

# VISUALIZING TYPES
print("--- Type Visualization ---")
print(f"Variable: user_age   | Value: {user_age}   | Type: {type(user_age)}")
print(f"Variable: high_score | Value: {high_score} | Type: {type(high_score)}")

# DYNAMIC TYPING: Python is flexible!
# (Imagine a box that can hold any shape)
data_point = "Observation 1"
print(f"\nBefore: {data_point} ({type(data_point)})")

data_point = 42.0 
print(f"After : {data_point} ({type(data_point)})")

"""
YOUR CHALLENGE:
1. Create a variable called 'ai_model_name' and set it to a string.
2. Create a variable called 'accuracy' and set it to a float.
3. Print them both using an f-string (like the examples above).
4. Try to write the 'cleanest' code possible!
"""
ai_model_name = ""
accuracy = 0.0
print(f"Variable: ai_model_name | Value: {ai_model_name} | Type: {type(ai_model_name)}")
print(f"Variable: accuracy | Value: {accuracy} | Type: {type(accuracy)}")
