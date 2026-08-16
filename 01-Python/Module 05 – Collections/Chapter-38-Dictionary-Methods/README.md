# Chapter 40 — Dictionary Methods

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
