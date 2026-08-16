# Chapter 41 — Dictionary Iteration

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
