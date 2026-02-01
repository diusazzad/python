# Debug Trace: Day 8 - Fixing Inheritance 🐞

This trace explains why the code crashed and how to "think" like Python when debugging class structures.

## 1. The Error Visualization (What Python Saw) 🛑

```mermaid
flowchart LR
    subgraph Wrong ["Current Error"]
        direction TB
        F1["Line 66: def CleaningRobot(Robot)"]
        F1 -- "Is interpreted as" --> F2["A FUNCTION named CleaningRobot"]
        Call["Line 73: CleaningRobot('Roomba', 50)"]
        Call -- "Triggers" --> Error["TypeError: Takes 1 arg, but 2 given"]
    end

    subgraph Right ["The Correction"]
        direction TB
        C1["Line 66: class CleaningRobot(Robot)"]
        C1 -- "Is interpreted as" --> C2["A CLASS named CleaningRobot"]
        Call2["Line 73: CleaningRobot('Roomba', 50)"]
        Call2 -- "Triggers" --> Init["__init__ constructor"]
    end
```

## 2. Symptom & Cure Table

| Symptom | The Cause | The Cure |
| :--- | :--- | :--- |
| **`TypeError: ... but 2 given`** | You used `def` instead of `class`. Functions view `Robot` as a variable, not a parent. | Change `def` to `class`. |
| **`AttributeError: 'NoneType' ...`** | Because your function didn't `return`, `roomba` became `None`. | Making it a `class` automatically returns the new object. |
| **`AttributeError: 'Robot' has no 'version'`** | Line 59 had a loose variable `self.version` with no value. | Either assign a value or remove the line. |

## 3. High-Fidelity UML Correction 📐

```mermaid
classDiagram
    class Robot {
        +String name
        +Int battery_level
        +charge() String
        +status() String
    }

    class CleaningRobot {
        +clean() String
    }

    Robot <|-- CleaningRobot : Correct Generalization
```
