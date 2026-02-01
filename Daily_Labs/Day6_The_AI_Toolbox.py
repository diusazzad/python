import random
import math as m
"""
DAILY LAB: DAY 6 - THE AI TOOLBOX
Topic: Modules (Importing code).

In AI, we don't build everything from scratch. We use "Modules"
(libraries) written by other geniuses.

Think of it like buying a pre-made engine for your car instead of
casting the metal yourself.

VISUAL REPRESENTATION:
[ Your Code ] <--- IMPORT --- [ Math Module ]
      |                             |
      +---- Uses 'sqrt' function ---+
"""


# 1. SIMPLE IMPORT

# 2. SPECIFIC IMPORT (Better for memory)
from datetime import datetime

print("--- AI System Diagnostics ---")

# Using the 'math' module for advanced logic
probability = 0.85
# Square root is common in AI error calculations
root_prob = m.sqrt(probability)

print(f"Original Prob: {probability}")
print(f"Square Root  : {root_prob:.4f}")

# Using the 'datetime' module
current_time = datetime.now()
print(f"System Check at: {current_time.strftime('%H:%M:%S')}")

"""
YOUR CHALLENGE:
1. Import the 'random' module.
2. Create a function 'generate_ai_score' that:
   - Uses 'random.random()' to get a number between 0 and 1.
   - Returns that number.
3. Import the 'math' module using 'import math as m' (this is called Aliasing).
4. Use 'm.floor()' to round down the number 9.99 and print it.
5. Bonus: Use your 'generate_ai_score' to create a list of 5 random scores!
"""
# import the random module


# use m.floor() to round down the number 9.99 and print it
print(m.floor(9.99))


# create a function 'generate_ai_score' that:
def generate_ai_score():
    return random.random()


# use your 'generate_ai_score' to create a list of 5 random scores!
for i in range(5):
    print(generate_ai_score())
