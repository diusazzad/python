"""
DAILY LAB: DAY 4 - STRUCTURED DATA
Topic: Dictionaries (Key-Value Pairs).

Lists are great for sequences, but Dictionaries are like real-world
objects. If a model predicts something, it doesn't just give a number;
it gives a structured "Object."

VISUAL REPRESENTATION:
Dictionary: { "key": "value" }
Example:    { "label": "Cat", "confidence": 0.98 }

Think of it like a real dictionary:
"Word" (Key) -> "Definition" (Value)
"""

# CLEAN CODE: Use descriptive names for your keys
ai_model_config = {
    "model_name": "Llama-3",
    "version": 1.5,
    "max_tokens": 2048,
    "is_active": True,
}

print(f"--- Model Profile: {ai_model_config['model_name']} ---")

# ACCESSING DATA
print(f"Version: {ai_model_config['version']}")

# ADDING/UPDATING DATA
ai_model_config["accuracy"] = 0.92  # New entry
ai_model_config["is_active"] = False  # Updating entry

# DICTIONARIES IN LOOPS
# (AI results often come as a list of dictionaries)
detections = [
    {"object": "Car", "confidence": 0.9},
    {"object": "Person", "confidence": 0.3},
    {"object": "Tree", "confidence": 0.8},
]

print("\nProcessing Batch Detections:")
for item in detections:
    # Accessing dict values inside a loop
    obj = item["object"]
    score = item["confidence"]

    if score > 0.5:
        print(f"Detected: {obj} (Certain)")
    else:
        print(f"Detected: {obj} (Uncertain - Ignoring)")

"""
YOUR CHALLENGE:
1. Create a dictionary called 'user_profile' with:
   - name (string)
   - learning_track (string)
   - current_day (integer)
2. Add a new key 'topics_learned' which is a LIST of 3 strings.
3. Print a sentence like: "User {name} is on day {current_day} learning {track}."
4. Bonus: Print the second item in your 'topics_learned' list using the dictionary.
"""
user_profile = {"name": "Sazzad", "learning_track": "AI", "current_day": 4}

user_profile["topics_learned"] = ["Python", "Data Science", "Machine Learning"]

print(
    f"User {user_profile['name']} is on day {user_profile['current_day']} learning {user_profile['learning_track']}"
)

# print(f"The second topic learned is: {user_profile['topics_learned']}") 

# pro way 
print(f"The second topic learned is: {user_profile['topics_learned'][1]}")


