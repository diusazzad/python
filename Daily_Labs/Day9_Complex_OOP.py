"""
# Day 9: Secret Codes & Modern Art (Encapsulation & Polymorphism)
# -------------------------------------------------------------
# Goals:
# 1. Private Variables (__) to protect sensitive AI data.
# 2. Polymorphism to make different AI models "behave" the same.
# 3. Clean Code: Using property decorators instead of manuals getters/setters.
"""


# --- 1. ENCAPSULATION (The Secret Room) ---
class SecretAI:
    def __init__(self, model_name, api_key):
        self.name = model_name
        self.__api_key = api_key  # Double underscore makes it PRIVATE
        self._usage_count = 0  # Single underscore is a GENTLEMAN'S limit (protected)

    # Use @property to make it look like a variable, but handle it like a function
    @property
    def usage(self):
        return f"This model has been used {self._usage_count} times."

    def run_query(self, key):
        if key == self.__api_key:
            self._usage_count += 1
            return f"[{self.name}] Query successful!"
        else:
            return "ACCESS DENIED: Internal Key Mismatch."


# --- 2. POLYMORPHISM (The Master Shape) ---
class RobotBase:
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")


class ChatBot(RobotBase):
    def speak(self):
        return "ChatBot: Hello! How can I help you today?"


class SecurityBot(RobotBase):
    def speak(self):
        return "SecurityBot: INTRUDER DETECTED! Identify yourself."


# This function doesn't care WHAT robot it is.
# It only cares that it HAS a .speak() method.
def activate_robot(robot):
    print(f"System Activation: {robot.speak()}")


# --- 🧪 EXECUTION ---
if __name__ == "__main__":
    print("--- 1. Encapsulation Demo ---")
    my_ai = SecretAI("Zeng-GPT", "SECRET_123")

    print(my_ai.name)  # Works fine (Public)
    # print(my_ai.__api_key) # ERROR! (Private)

    print(my_ai.run_query("WRONG_KEY"))
    print(my_ai.run_query("SECRET_123"))
    print(my_ai.usage)  # Using @property

    print("\n--- 2. Polymorphism Demo ---")
    bots = [ChatBot(), SecurityBot()]

    for b in bots:
        activate_robot(b)

# --- 🚀 CHALLENGE FOR YOU ---
# 1. Create a class called 'BankAccount'.
# 2. Make '__balance' private.
# 3. Use @property to let the user see the balance.
# 4. Create a method 'deposit(amount)' that adds to the balance ONLY IF amount > 0.
# 5. Create a method 'withdraw(amount)' that subtracts ONLY IF balance is enough.
# 6. Then, create a class 'CryptoWallet' and a class 'GoldVault'.
# 7. Give both a method 'get_value()' that returns their worth.
# 8. Create a loop that prints the value of both, showing POLYMORPHISM.

