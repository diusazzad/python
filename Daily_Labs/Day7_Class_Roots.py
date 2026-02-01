"""
DAILY LAB: DAY 7 - CLASS ROOTS
Topic: Classes and Objects (Introduction to OOP).

In AI, every model is a "Class". A Class is a BLUEPRINT (like a
drawing of a house) and an Object is the actual HOUSE built from it.

VISUAL REPRESENTATION:
[ Class: AIModel ] (The Blueprint)
      |
      +---- Property: name
      +---- Method: predict()
      |
 [ Object: MyModel1 ] (The Reality)

--- �️ DIAGRAM BREAKDOWN (Python Tutor Style) �️ ---
1. GLOBAL FRAME: Contains 'AIModel' (the class) and 'my_brain' (vairable).
2. OBJECTS: 
   - 'AIModel class': The blueprint containing methods (__init__, status_report).
   - 'AIModel instance': The actual box in memory containing 'name' and 'version'.
3. POINTERS: Notice how 'my_brain' points to the 'AIModel instance'.
4. THE 'SELF' FRAME: When status_report runs, a NEW frame appears. 
   'self' inside that frame points to the SAME 'AIModel instance'.
-------------------------------------------------------
"""


# CLEAN CODE: Use PascalCase for Class names
class AIModel:
    def __init__(self, name, version):
        """
        The __init__ method is a 'Constructor'.
        It sets up the model when it's first created.
        """
        self.name = name  # Property
        self.version = version  # Property
        self.is_active = False  # Default Property

    def status_report(self):
        """A 'Method' is a function that belongs to a class."""
        state = "Active" if self.is_active else "Standby"
        return f"Model: {self.name} (v{self.version}) -> {state}"


# CREATING THE OBJECT
my_brain = AIModel("DeepThinker", 1.0)

# ACCESSING PROPERTIES
print("--- AI Management Console ---")
print(my_brain.status_report())

# UPDATING PROPERTIES
my_brain.is_active = True
print(my_brain.status_report())

"""
YOUR CHALLENGE:
1. Create a class called 'Robot'.
2. Give it an '__init__' with 'name' and 'battery_level'.
3. Create a method 'charge()' that sets 'battery_level' to 100.
4. Create an object named 'my_bot' with 50% battery.
5. Print its status, charge it, and print its status again!
"""
class Robot:
    def __init__(self, name, battery_level):
        self.name = name
        self.battery_level = battery_level

    def charge(self):
        self.battery_level = 100

    def status(self):
        return f"{self.name} has {self.battery_level}% battery."

my_bot = Robot("Wall-E", 50)
print(my_bot.status())
my_bot.charge()
print(my_bot.status())
