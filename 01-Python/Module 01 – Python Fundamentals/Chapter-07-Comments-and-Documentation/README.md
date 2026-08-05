# Chapter 07 - Comments & Documentation

## 🎯 Learning Objectives

By the end of this chapter, you will be able to:

- Understand comments and their purpose
- Write single-line comments
- Understand multi-line comments
- Write docstrings for functions
- Follow documentation best practices

---

# What is a Comment?

A comment is text that Python ignores during execution.

Comments are written for humans to improve code readability.

Example:

```python
# This is a comment

print("Hello")
```

---

# Why Use Comments?

Comments help explain:

- Business logic
- Complex algorithms
- Assumptions
- Design decisions
- Future improvements

---

# Single-Line Comments

Use the `#` symbol.

```python
# Store employee salary
salary = 50000
```

---

# Multi-Line Comments

Python commonly uses triple quotes for longer descriptions.

```python
"""
This program calculates
the total salary.
"""
```

Although these are string literals, they are often used as multi-line comments.

---

# Docstrings

A docstring documents a function, class, or module.

Example:

```python
def add(a, b):
    """
    Returns the sum of two numbers.
    """
    return a + b
```

Docstrings improve readability and can be accessed using tools like `help()`.

---

# Comments vs Docstrings

| Comments | Docstrings |
|----------|------------|
| Begin with `#` | Use triple quotes |
| Explain code | Document functions, classes, and modules |
| Ignored during execution | Stored as documentation |

---

# Best Practices

- Explain **why**, not **what**.
- Use meaningful variable names.
- Keep comments up to date.
- Write docstrings for reusable code.
- Remove obsolete comments.

---

# AI Connection

AI projects rely on good documentation.

Example:

```python
# Load the language model
model = pipeline("text-generation")

# Read user prompt
prompt = input("Ask a question: ")

# Generate response
result = model(prompt)
```

---

# Key Takeaways

- Comments improve code readability.
- Python ignores comments during execution.
- Docstrings document functions, classes, and modules.
- Good comments explain the reasoning behind code.
- Clean, readable code reduces the need for excessive comments.

---

# Interview Questions

1. What is a comment?
2. What is a docstring?
3. What is the difference between comments and docstrings?
4. Why are comments important?
5. What are the best practices for writing comments?

---

# Assignment

## Practical

- Write a program using comments.
- Create a function with a docstring.
- Practice writing meaningful variable names.

## Theory

1. Why are comments useful?
2. When should comments be avoided?
3. What is the purpose of a docstring?

---

# Summary

- Comments help humans understand code.
- Docstrings document reusable components.
- Well-written code and meaningful names reduce the need for unnecessary comments.
- Documentation is an essential skill for professional software development.