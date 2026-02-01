# Visual Trace: Day 7 - Class Roots 🤖

This diagram recreates the internal state of Python's memory as you saw in the Python Tutor screenshot.

## 1. Memory Layout (Frames vs. Objects)

```mermaid
graph LR
    subgraph Frames [Frames]
        direction TB
        GF["Global Frame"]
        SRF["status_report Frame"]
    end

    subgraph Objects [Objects in Memory]
        direction TB
        AMC["AIModel (Class Blueprint)<br/>---<br/>__init__<br/>status_report"]
        AMI["AIModel Instance (The Box)<br/>---<br/>is_active: True<br/>name: 'DeepThinker'<br/>version: 1.0"]
    end

    GF -- "AIModel" --> AMC
    GF -- "my_brain" --> AMI
    SRF -- "self" --> AMI
    SRF -- "Return Value" --> RV["'Model: DeepThinker (v1.0) -> Active'"]
```

## 2. The Relationship Matrix

| Frame | Variable | Pointer Destination | Why? |
| :--- | :--- | :--- | :--- |
| **Global** | `my_brain` | `AIModel instance` | This is your main handle for the object. |
| **status_report** | `self` | `AIModel instance` | `self` is just the function's way of reaching the box. |
| **Global** | `AIModel` | `AIModel class` | Points to the blueprint so you can make more. |

## 4. Logic Flowchart (Code Visualizer Style) 📊
This shows how the code "moves" from line to line, jumping into functions and back out.

```mermaid
flowchart TD
    Start([Start]) --> L35["Line 35: Create my_brain instance"]
    L35 --> Init["__init__(self, name, version)"]
    Init --> SetName["self.name = name"]
    SetName --> SetVer["self.version = version"]
    SetVer --> SetAct["self.is_active = False"]
    SetAct --> EndInit([Return to Main])
    
    EndInit --> L39["Line 39: Print Console Header"]
    L39 --> L40["Line 40: Call status_report()"]
    
    L40 --> SR["status_report(self)"]
    SR --> CalcState["Check if is_active"]
    CalcState --> RetString["Return 'Model: ...'"]
    RetString --> L40_Print["Print returned string"]
    
    L40_Print --> L43["Line 43: Set is_active = True"]
    L43 --> L44["Line 44: Call status_report() again"]
    L44 --> End([End of Script])

    style Init fill:#f9f,stroke:#333,stroke-width:2px
    style SR fill:#f9f,stroke:#333,stroke-width:2px
```

## 5. Call Hierarchy
- `Main Script`
    - `AIModel.__init__`
    - `AIModel.status_report`
    - `AIModel.status_report`
