"""
DAILY LAB: DAY 5 - NEURAL FUNCTIONS
Topic: Functions (Def, Arguments, and Return).

In AI, a function is like a "Module" in a Neural Network. 
It takes an INPUT (like an image), PROCESSES it, and gives an OUTPUT (a prediction).

VISUAL REPRESENTATION:
      [ Input ] (Argument)
          |
    +-----+-----+
    |  FUNCTION | (The "Brain")
    +-----+-----+
          |
     [ Output ] (Return Value)
"""

# CLEAN CODE: Use verbs for function names
def predict_emotion(score):
    """
    Simulates an AI model predicting emotion from a sentiment score.
    """
    if score > 0.8:
        return "Happy"
    elif score > 0.4:
        return "Neutral"
    else:
        return "Sad"

# USING THE FUNCTION
user_sentiment = 0.95
result = predict_emotion(user_sentiment)

print(f"--- AI Emotion Analyzer ---")
print(f"Input Score: {user_sentiment}")
print(f"Prediction : {result}")

# MULTIPLE ARGUMENTS
def calculate_accuracy(correct, total):
    if total == 0:
        return 0
    return (correct / total) * 100

final_acc = calculate_accuracy(85, 100)
print(f"\nModel Accuracy: {final_acc}%")

"""
YOUR CHALLENGE:
1. Create a function called 'process_temperature' that takes one argument 'temp'.
   - If temp > 100, return "HOT"
   - Otherwise, return "OK"
2. Create a list of 3 temperatures.
3. Use a 'for-loop' to call your function for each temperature and print the result.
4. Bonus: Create a function 'get_greeting' that takes 'name' and 'time_of_day' 
   and returns a full greeting string!
"""

def process_temperature(temp):
    if temp > 100:
        return "HOT"
    else:
        return "OK"

temperatures = [22.5,18.0,25.3]

for temp in temperatures:
    print(f"Temparatures: {temp} -> {process_temperature(temp)}")
# get_greeting
def get_greeting(name,time_of_day):
    return f"Good {time_of_day} {name}"
    