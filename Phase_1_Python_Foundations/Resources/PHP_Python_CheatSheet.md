# PHP → Python Quick Reference

## Variables

```php
// PHP
$name = "John";
$age = 25;
$is_active = true;
```

```python
# Python
name = "John"
age = 25
is_active = True
```

---

## Strings

```php
// PHP
echo "Hello $name";
$len = strlen($text);
$lower = strtolower($text);
$upper = strtoupper($text);
$pos = strpos($text, "lo");
$replace = str_replace("old", "new", $text);
$split = explode(",", $text);
$join = implode("-", $array);
```

```python
# Python
print(f"Hello {name}")
length = len(text)
lower = text.lower()
upper = text.upper()
pos = text.find("lo")  # returns -1 if not found
replace = text.replace("old", "new")
split = text.split(",")
join = "-".join(list)
```

---

## Arrays ↔ Lists

```php
// PHP
$arr = [1, 2, 3];
$arr[] = 4;
array_push($arr, 5);
$count = count($arr);
$last = array_pop($arr);
$first = array_shift($arr);
sort($arr);
$exists = in_array(1, $arr);
$keys = array_keys($dict);
```

```python
# Python
arr = [1, 2, 3]
arr.append(4)
arr.extend([5])
count = len(arr)
last = arr.pop()
first = arr.pop(0)  # or arr[0] then remove
arr.sort()
exists = 1 in arr
keys = list(dict.keys())
```

---

## Dictionaries

```php
// PHP
$dict = ["name" => "John", "age" => 25];
$dict["city"] = "NYC";
$keys = array_keys($dict);
$values = array_values($dict);
$exists = isset($dict["name"]);
unset($dict["age"]);
```

```python
# Python
dict = {"name": "John", "age": 25}
dict["city"] = "NYC"
keys = dict.keys()
values = dict.values()
exists = "name" in dict
del dict["age"]
# or dict.pop("age")
```

---

## Loops

```php
// PHP
foreach ($arr as $item) { }
foreach ($dict as $k => $v) { }
for ($i = 0; $i < 10; $i++) { }
```

```python
# Python
for item in arr:
for k, v in dict.items():
for i in range(10):
```

---

## Functions

```php
// PHP
function greet($name) {
    return "Hello $name";
}
$greet = function($name) { return "Hello $name"; };
```

```python
# Python
def greet(name):
    return f"Hello {name}"

greet = lambda name: f"Hello {name}"
```

---

## Conditionals

```php
// PHP
if ($x > 10) {
    echo "big";
} elseif ($x > 5) {
    echo "medium";
} else {
    echo "small";
}
```

```python
# Python
if x > 10:
    print("big")
elif x > 5:
    print("medium")
else:
    print("small")
```

---

## Type Checking

```php
// PHP
gettype($var);
is_string($var);
is_int($var);
is_array($var);
```

```python
# Python
type(var)
isinstance(var, str)
isinstance(var, int)
isinstance(var, list)
```

---

## Input

```php
// PHP
$input = trim(fgets(STDIN));
```

```python
# Python
user_input = input("Prompt: ")  # Always returns string!
```

---

## Key Differences

| PHP | Python |
|-----|--------|
| `$` prefix | No prefix |
| `{}` for blocks | Indentation (spaces/tabs) |
| `echo` | `print()` |
| `true/false` | `True/False` |
| `null` | `None` |
| `.` concatenation | `+` or f-strings |
| `array_push` | `.append()` |
| `count()` | `len()` |
| `in_array()` | `in` |
| `array_map` | List comprehension |
