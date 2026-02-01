"""
DAILY LAB: DAY 2 - NEURAL LOGIC
Topic: Comparisons and If-Else (Decision Making).

AI is essentially a series of complex decisions. If a probability 
is > 0.5, we say it's a "Cat". If not, it's a "Dog".

VISUAL REPRESENTATION:
      [ Input ]
          |
    < Is x > 10? > --- YES ---> [ Process A ]
          |
          NO
          |
    [ Process B ]
"""

# CLEAN CODE: Use clear boolean names
is_model_trained = True
confidence_score = 0.85

print("--- AI Decision Engine ---")

if confidence_score > 0.9:
    print("Decision: High Certainty")
elif confidence_score > 0.5:
    print("Decision: Moderate Certainty")
else:
    print("Decision: Low Certainty - Needs Retraining")

# LOGICAL OPERATORS: combining conditions
# (Critical for filtering data later!)
if is_model_trained and confidence_score > 0.7:
    print("\nSystem: Ready for Deployment")

"""
YOUR CHALLENGE:
1. Create a variable 'temperature' (integer).
2. Write an if-else block:
   - If temp > 100: print "System Overheat!"
   - If temp < 0: print "System Frozen!"
   - Otherwise: print "System Operational."
3. Bonus: Use a boolean variable 'is_fan_on' to check:
   - If temperature > 80 AND is_fan_on is False: print "Warning: Turn on fan!"
"""

temperature = 101

if temperature > 10:
    print("System Overheat!")
elif temperature < 0:
    print("System Frozen!")
else:
    print("System Operational.")

is_fan_on = False

if temperature > 80 and is_fan_on == False:
    print("Warning: Turn on fan!")  
    

