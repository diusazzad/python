"""
DAILY LAB: DAY 8 - THE FAMILY TREE
Topic: Class Inheritance (Base vs. Subclass).

In AI, we often have a general base (like 'Module') and then
specific children (like 'LinearLayer' or 'ConvLayer').

Inheritance lets a "Child" class take all the powers of a "Parent"
class and add its own unique features.

VISUAL REPRESENTATION:
      [ Parent: Device ]
             |
      +------+------+
      |             |
[ Child: Phone ] [ Child: AI_Robot ]
"""


class Device:
    def __init__(self, brand):
        self.brand = brand
        self.is_on = False

    def power_on(self):
        self.is_on = True
        return f"{self.brand} is now ON."


# INHERITANCE: AI_Robot inherits from Device
class AI_Robot(Device):
    def __init__(self, brand, model_type):
        # 'super()' calls the Parent's __init__
        super().__init__(brand)
        self.model_type = model_type

    def think(self):
        return f"The {self.model_type} is processing data..."


# DEMO
my_ai = AI_Robot("Google", "Gemini-Bot")
print("--- Inheritance Demo ---")
print(my_ai.power_on())  # Notice: AI_Robot has power_on because of its parent!
print(my_ai.think())

"""
YOUR CHALLENGE:
1. Use your 'Robot' class from Day 7 as the Parent (You can copy it here).
2. Create a Child class called 'CleaningRobot' that inherits from 'Robot'.
3. Give the Child a new method 'clean()' that returns "Cleaning the room...".
4. Create an object 'roomba' from 'CleaningRobot'.
5. Show that 'roomba' can both 'charge()' (Parent power) AND 'clean()' (Child power)!
"""


class Robot:
    def __init__(self, name, battery_level):
        self.name = name
        self.battery_level = battery_level

    def charge(self):
        self.battery_level = 100
        return f"{self.name} is now fully charged!"

    def status(self):
        return f"Name: {self.name} | Battery: {self.battery_level}%"


class CleaningRobot(Robot):
    def __init__(self, name, battery_level):
        super().__init__(name, battery_level)

    def clean(self):
        return f"The {self.name} is cleaning the room..."


roomba = CleaningRobot("Roomba", 50)
print("--- Challenge Demo ---")
print(roomba.status())
print(roomba.clean())
print(roomba.charge())
print(roomba.status())
