# Visual Guide: Dictionaries (Key-Value Pairs) 🗺️

In mathematics and AI, we call this a **Mapping**. It’s like a function where you provide an input (Key) and get a specific output (Value).

## 1. The Mathematical view
If $f(x) = y$, then in a dictionary:
- $x$ is the **Key**
- $y$ is the **Value**

For example:
$f(\text{"model"})$ = "Llama-3"
$f(\text{"accuracy"})$ = 0.95

## 2. The Structural Layout (Mermaid Diagram)

```mermaid
graph LR
    subgraph Dictionary ["User Profile Dictionary"]
        direction TB
        K1["'name'"] -- Points to --> V1["'Sazzad'"]
        K2["'track'"] -- Points to --> V2["'AI Mastery'"]
        K3["'day'"] -- Points to --> V3["4"]
    end
```

## 3. List vs. Dictionary (The Big Difference)

| Feature | List (Container) | Dictionary (Labeler) |
| :--- | :--- | :--- |
| **How to find data** | By Position (Index: 0, 1, 2) | By Name (Label: "name", "id") |
| **Analogy** | A row of lockers with numbers | A shelf of labeled folders |
| **AI Use Case** | Storing raw pixel values | Storing model settings/results |

## 4. Nested Structure (The AI Reality)
In real AI projects, dictionaries often hold lists!

```mermaid
graph TD
    A["Detection Object"] --> B["'label': 'Car'"]
    A --> C["'boxes': [10, 20, 50, 80]"]
    C --> D["x-coordinate"]
    C --> E["y-coordinate"]
    C --> F["width"]
    C --> G["height"]
```
