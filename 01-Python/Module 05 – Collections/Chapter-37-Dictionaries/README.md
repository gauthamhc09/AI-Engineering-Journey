# Module 05 — Dictionary Notes (Chapters 37, 38, 39, 40)

## 1. What is a Dictionary?
A dictionary stores data as **key-value pairs**.

```python
student = {
    "name": "Rahul",
    "age": 25,
    "course": "Python"
}
```

- Keys identify data.
- Keys must be unique.
- Values can be any suitable Python object.
- Dictionaries are mutable.

### Accessing values
```python
student["name"]          # Rahul
student.get("name")      # Rahul
student.get("city")      # None
student.get("city", "Bengaluru")
```

`[]` raises `KeyError` for a missing key; `.get()` safely returns `None` or a default.

### Add / Update
```python
student["city"] = "Bengaluru"   # add
student["age"] = 26             # update
student.update({"age": 27, "city": "Mysuru"})
```

### Removing
```python
del student["age"]
student.pop("city")       # removes specific key, returns value
student.popitem()         # removes last inserted pair
student.clear()           # empties dictionary
```

## 2. Nested Dictionaries
```python
employee = {
    "name": "Anita",
    "address": {
        "city": "Bengaluru",
        "state": "Karnataka"
    }
}

employee["address"]["city"]
```

A dictionary can contain lists and other dictionaries.

## 3. Dictionaries + Lists
```python
portfolio = {
    "investor": "Gautham",
    "stocks": ["INFY", "TCS", "ITC"]
}
```

A common API-style structure is a list of dictionaries:
```python
employees = [
    {"name": "Anita", "salary": 1200000},
    {"name": "Rahul", "salary": 1000000}
]
```

Access:
```python
employees[0]["name"]
```

## Key Takeaways
- Dictionary = key → value
- Keys are unique.
- Use `[]` when the key must exist; `.get()` when it may be missing.
- Dictionaries are excellent for structured records and JSON/API data.


---

## Important Methods

| Method | Purpose |
|---|---|
| `.get(key, default)` | Safely retrieve a value |
| `.keys()` | Get dictionary keys |
| `.values()` | Get dictionary values |
| `.items()` | Get key-value pairs |
| `.update()` | Add/update multiple entries |
| `.copy()` | Create a shallow copy |
| `.pop(key)` | Remove a specific key and return its value |
| `.popitem()` | Remove the last inserted pair |
| `.clear()` | Remove all entries |

### Examples
```python
employee.get("city", "Unknown")

employee.update({
    "salary": 90000,
    "city": "Bengaluru"
})

copy_employee = employee.copy()

salary = employee.pop("salary")
employee.popitem()
employee.clear()
```

### `.copy()` vs assignment
```python
copy1 = employee.copy()   # separate dictionary
copy2 = employee          # same dictionary object
```

`.copy()` is a **shallow copy**.

## Key Takeaways
- Use `.get()` for optional keys.
- Use `.update()` for multiple changes.
- Use `.pop()` when you need the removed value.
- Use `.copy()` when you need a separate outer dictionary.


---

Given:
```python
employee = {
    "name": "Anita",
    "age": 30,
    "department": "AI"
}
```

## Loop Through Keys
```python
for key in employee:
    print(key)
```

Direct iteration over a dictionary produces **keys**.

Explicit version:
```python
for key in employee.keys():
    print(key)
```

## Loop Through Values
```python
for value in employee.values():
    print(value)
```

## Loop Through Key-Value Pairs
```python
for key, value in employee.items():
    print(key, value)
```

`.items()` produces pairs such as:
```python
("name", "Anita")
("age", 30)
```

Python unpacks each pair into `key` and `value`.

## Membership
```python
"name" in employee          # True
"salary" not in employee   # True
```

Dictionary membership normally checks **keys**.

To check values:
```python
"Anita" in employee.values()
```

## Practical Pattern
For a list of dictionaries:
```python
for employee in employees:
    if employee["salary"] > 1000000:
        print(employee["name"])
```

## Key Takeaways
- `for key in dictionary` → keys
- `.values()` → values
- `.items()` → key-value pairs
- `in` normally checks dictionary keys


---

Dictionary comprehension creates dictionaries concisely from an iterable.

## Basic Syntax
```python
{
    key: value
    for item in iterable
}
```

Example:
```python
squares = {
    number: number * number
    for number in range(1, 6)
}
```

Result:
```python
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

## With a Condition
```python
even_squares = {
    number: number * number
    for number in range(1, 11)
    if number % 2 == 0
}
```

## Using `.items()`
```python
prices = {
    "INFY": 1500,
    "TCS": 3500,
    "ITC": 500
}

expensive = {
    symbol: price
    for symbol, price in prices.items()
    if price > 1500
}
```

Result:
```python
{"TCS": 3500}
```

## Normal Loop Equivalent
```python
result = {}

for number in range(1, 6):
    result[number] = number * 10
```

Equivalent:
```python
result = {
    number: number * 10
    for number in range(1, 6)
}
```

## Practical Nested Data Example
```python
holdings = [
    {"symbol": "INFY", "value": 30000},
    {"symbol": "TCS", "value": 35000}
]

pnl_like_map = {
    stock["symbol"]: stock["value"]
    for stock in holdings
}
```

## Key Takeaways
- Dictionary comprehension produces `key: value`.
- Add `if` after the `for` to filter.
- Understand the normal loop first.
- Prefer readability over forcing everything into one line.


---

