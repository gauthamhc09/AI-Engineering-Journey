# Chapter 09 - Type Casting

## 🎯 Learning Objectives

By the end of this chapter, you will be able to:

- Understand type casting
- Perform implicit and explicit conversions
- Convert between common Python data types
- Understand truthy and falsy values
- Avoid common type conversion mistakes

---

# What is Type Casting?

Type casting is the process of converting one data type into another.

Example:

```python
age = "25"

age = int(age)
```

---

# Types of Type Conversion

## Implicit Conversion

Performed automatically by Python.

Example:

```python
print(10 + 5.5)
```

Output:

```
15.5
```

Python converts `10` to `10.0` automatically.

---

## Explicit Conversion

Performed manually by the programmer.

Examples:

```python
int("25")

float(10)

str(100)

bool(1)
```

---

# Common Conversion Functions

| Function | Converts To |
|----------|-------------|
| `int()` | Integer |
| `float()` | Float |
| `str()` | String |
| `bool()` | Boolean |

---

# Truthy and Falsy Values

Falsy values:

```python
False
0
0.0
""
[]
{}
set()
None
```

Most other values evaluate to `True`.

Examples:

```python
bool("")
# False

bool("Python")
# True

bool(0)
# False

bool(1)
# True
```

---

# Invalid Conversions

Example:

```python
int("hello")
```

Raises:

```
ValueError
```

---

# AI Connection

LLM applications often convert user input before sending it to a model.

Example:

```python
temperature = float(input("Temperature: "))

max_tokens = int(input("Max Tokens: "))
```

Correct data types are essential for APIs and machine learning models.

---

# Key Takeaways

- Type casting changes one data type into another.
- Python supports implicit and explicit conversion.
- Use `int()`, `float()`, `str()`, and `bool()` frequently.
- Understand truthy and falsy values.
- Validate user input before converting it.

---

# Interview Questions

1. What is type casting?
2. What is the difference between implicit and explicit conversion?
3. Explain truthy and falsy values.
4. Why does `bool("False")` return `True`?
5. Why is type conversion important in AI applications?

---

# Assignment

## Practical

- Practice all common conversions.
- Experiment with truthy and falsy values.

## Theory

1. Explain type casting.
2. Explain implicit vs explicit conversion.
3. Explain truthy and falsy values.

---

# Summary

- Type casting converts data from one type to another.
- Implicit conversion is automatic.
- Explicit conversion is performed manually.
- Understanding conversions prevents many common programming errors.
- Type conversion is widely used in APIs, databases, and AI systems.