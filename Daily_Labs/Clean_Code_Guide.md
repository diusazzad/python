# The Clean Code Guide 🎨
*Mastering AI starts with writing code that is easy to read and maintain.*

## 1. Naming is Everything
Use descriptive names. Tell a story with your variables.
- ❌ `a = "John"`
- ✅ `student_name = "John"`

## 2. The DRY Principle
**D**on't **R**epeat **Y**ourself. If you write the same code twice, put it in a function.

## 3. KISS
**K**eep **I**t **S**imple, **S**tupid. Don't make code complex just to look "smart." The best AI code is simple.

## 4. Visual Layout
- Use blank lines to separate "paragraphs" of logic.
- Keep lines under 79-88 characters (standard practice).
- Add clear comments explaining *why*, not just *what*.

## 5. Explicit is Better than Implicit
Be clear about what your code does.
- ❌ `x = [i for i in range(10) if i % 2 == 0]`
- ✅ 
```python
# Create a list of even numbers from 0 to 9
numbers = range(10)
even_numbers = [num for num in numbers if num % 2 == 0]
```
