# Advanced UML Trace: Day 8 - Inheritance 🌲

This diagram follows the **Enterprise UML Standard** to show exactly how properties and methods are shared across the system.

## 1. Enterprise UML Class Diagram 📐

```mermaid
classDiagram
    class Device {
        -String brand
        -Boolean is_on
        +power_on() String
    }

    class AI_Robot {
        -String model_type
        +think() String
    }

    class Sensor {
        -String type
        -Float sensitivity
    }

    Device <|-- AI_Robot : Generalization (Inheritance)
    AI_Robot *-- Sensor : 1..* Composition (Robot HAS Sensors)
    
    note for Device "Parent Class: Defines basic identity"
    note for AI_Robot "Child Class: Adds AI logic"
    note for Sensor "Helper Class: Used by AI_Robot"
```

## 2. UML Symbol Key (How to Read Like a Pro) 🔍

| Symbol | Name | Meaning in AI |
| :--- | :--- | :--- |
| **`-`** | Private | This data is "hidden" inside the object (Encapsulation). |
| **`+`** | Public | This is an action anyone can call (API). |
| **` <|-- `** | Inheritance | The child "IS A" type of the parent. |
| **` *-- `** | Composition | The parent "OWNS" the child (It can't exist without it). |
| **` 1..* `** | Multiplicity | One Robot can have 1 or more Sensors. |

## 3. The Object Matrix (Memory State)
When you create `my_ai = AI_Robot("Google", "Gemini")`:

```mermaid
stateDiagram-v2
    [*] --> Creation
    Creation --> ParentInit: calls super().__init__()
    ParentInit --> ChildInit: returns to AI_Robot
    ChildInit --> Ready: Object 0x123 is built
    
    state "0x123: AI_Robot Instance" as Ready {
        brand: "Google"
        is_on: False
        model_type: "Gemini"
    }
```
