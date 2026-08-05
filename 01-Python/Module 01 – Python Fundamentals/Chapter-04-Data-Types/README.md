# Chapter 04 - Data Types

## 🎯 Learning Objectives

By the end of this chapter, you will be able to:

- Understand what data types are
- Learn Python's built-in data types
- Use the `type()` function
- Perform type conversion
- Understand how data types are used in AI applications

---

# What is a Data Type?

A data type defines the kind of value a variable refers to.

Examples:

- Number
- Text
- Boolean
- No Value

Python uses data types to determine how values can be stored and manipulated.

---

# Built-in Data Types

| Data Type | Description | Example |
|-----------|-------------|---------|
| `int` | Whole numbers | `10` |
| `float` | Decimal numbers | `3.14` |
| `str` | Text | `"Hello"` |
| `bool` | True or False | `True` |
| `NoneType` | Represents no value | `None` |

---

# Integer (`int`)

Stores whole numbers.

```python
age = 33
```

Examples:

- Age
- Quantity
- Number of users
- Epochs in AI training

---

# Float (`float`)

Stores decimal numbers.

```python
learning_rate = 0.001
```

Examples:

- Height
- Accuracy
- Loss
- Learning rate

---

# String (`str`)

Stores text.

```python
name = "Gautham"
```

Everything inside quotes is a string.

Examples:

- Name
- City
- Prompt
- AI response

---

# Boolean (`bool`)

Stores either `True` or `False`.

```python
is_logged_in = True
```

Used for decisions and status flags.

---

# None (`NoneType`)

Represents the absence of a value.

```python
email = None
```

Often used as a placeholder until a value is available.

---

# Checking Data Types

Use the `type()` function.

```python
print(type(10))
print(type(3.14))
print(type("Python"))
print(type(True))
print(type(None))
```

---

# Type Conversion

Convert between data types.

```python
int("25")
float(10)
str(100)
int(5.9)
```

Remember:

```python
int(5.9)
```

returns:

```text
5
```

The decimal part is discarded.

---

# Common Mistakes

Incorrect:

```python
age = "30"
print(age + 5)
```

Correct:

```python
age = int(age)
print(age + 5)
```

---

# AI Connection

LLM applications use these data types everywhere.

```python
prompt = "Explain AI"

temperature = 0.7

max_tokens = 512

stream = True

response = None
```

---

# Key Takeaways

- Python supports multiple built-in data types.
- Data types determine how values behave.
- `type()` returns the data type of an object.
- Type conversion changes one type into another.
- Understanding data types is essential for AI and LLM development.

---

# Interview Questions

1. What is a data type?
2. Explain `int`, `float`, `str`, `bool`, and `None`.
3. What does `type()` do?
4. What is type conversion?
5. Why is `None` useful?

---

# Assignment

## Practical

- Create variables for all five data types.
- Print their values and types.
- Perform type conversions.

## Theory

1. What is a data type?
2. Why are data types important?
3. Explain type conversion with examples.
4. Where are data types used in AI?

---

# Summary

- Data types describe the kind of data stored.
- Python provides several built-in types.
- The most common are `int`, `float`, `str`, `bool`, and `NoneType`.
- Type conversion is a common operation in Python programs.
- These data types form the foundation of AI and LLM applications.