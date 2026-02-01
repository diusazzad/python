"""
DAILY LAB: DAY 3 - ITERATING DATA
Topic: Lists (Arrays) and For-Loops.

In AI, we rarely work with one number. we work with LISTS of data 
(like 1,000 images or 1,000,000 stock prices).

VISUAL REPRESENTATION:
Lists: [ "Cat", "Dog", "Bird" ]
          0       1       2    <-- Index (Position)

Loop:
FOR each item IN list:
    DO something to item
"""

# CLEAN CODE: Use plural names for lists
prediction_scores = [0.85, 0.12, 0.99, 0.45]

print("--- AI Batch Processing ---")

# The classic 'for' loop
for score in prediction_scores:
    if score > 0.5:
        print(f"Score {score}: High confidence!")
    else:
        print(f"Score {score}: Low confidence.")

# TRANSFORMING DATA: Creating a new list
# (AI models often normalize data)
normalized_scores = []
for score in prediction_scores:
    # Example: Simple shift
    new_score = score * 100
    normalized_scores.append(new_score)

print(f"\nOriginal: {prediction_scores}")
print(f"Shifted : {normalized_scores}")

"""
YOUR CHALLENGE:
1. Create a list called 'device_temperatures' with 5 numbers.
2. Write a for-loop to check each temperature:
   - If temp > 100, print "Alert: Device {temp} is overheating!"
   - Otherwise, print "Device {temp} is safe."
3. Bonus: Calculate the 'average_temperature' of the list.
   (Hint: sum(list) / len(list))
"""
device_temperatures = [101, 98, 102, 99, 100]
for temp in device_temperatures:
    if temp > 100:
        print(f"Alert: Device {temp} is overheating!")
    else:
        print(f"Device {temp} is safe.")

avarage_temparature = sum(device_temperatures) / len(device_temperatures)
print(f"Average Temperature: {avarage_temparature}")