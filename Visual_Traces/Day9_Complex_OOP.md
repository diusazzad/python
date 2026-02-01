# Visual Trace: Day 9 - Secret Codes & Modern Art 🎨

## 1. Encapsulation: The "Private Room" 🔒
Think of a class like a high-security AI Lab. Not everyone should touch the `raw_data`.

```mermaid
graph TD
    User((User))
    subgraph AILab ["Class: SecuritySystem"]
        Public[".start_system() - Public"]
        Private["__security_key - PRIVATE"]
        Logic{"Verification"}
    end

    User -- "Can call" --> Public
    User -- "X CANNOT TOUCH X" --> Private
    Public --> Logic
    Logic -- "Accesses" --> Private
```

## 2. Polymorphism: The "Master Interface" 🎭
In AI, we often swap models. Polymorphism allows us to call `predict()` on any model without knowing its type.

```mermaid
classDiagram
    class Model {
        <<interface>>
        +predict(data)
    }
    class CNN {
        +predict(data)
    }
    class Transformer {
        +predict(data)
    }

    Model <|-- CNN
    Model <|-- Transformer

    Note for Model "The 'Shape' is the same,\nthe 'Brain' inside is different."
```
