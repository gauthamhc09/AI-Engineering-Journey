# Chapter 11 - The `if` Statement

## 🎯 Learning Objectives

By the end of this chapter, you will:

- Understand control flow
- Learn the `if` statement
- Write Boolean expressions
- Understand indentation
- Apply `if` in real-world programs

---

# What is Control Flow?

Control flow determines which parts of a program execute based on conditions.

Without control flow, every statement executes sequentially.

With control flow, Python can make decisions.

---

# What is an `if` Statement?

An `if` statement executes a block of code only if its condition evaluates to `True`.

Syntax:

```python
if condition:
    # code
```

---

# Boolean Expressions

Conditions evaluate to either:

- `True`
- `False`

Examples:

```python
10 > 5
20 == 20
15 >= 18
```

---

# Example

```python
age = 20

if age >= 18:
    print("Eligible to Vote")
```

---

# Indentation

Python uses indentation to define blocks of code.

Correct:

```python
if age >= 18:
    print("Eligible")
```

Incorrect:

```python
if age >= 18:
print("Eligible")
```

---

# Multiple Statements

```python
if marks >= 90:
    print("Excellent")
    print("Keep Learning")
```

---

# AI Connection

AI systems frequently use `if` statements.

Example:

```python
if confidence >= 0.90:
    print("High Confidence")
```

---

# Common Mistakes

- Using `=` instead of `==`
- Forgetting the colon (`:`)
- Incorrect indentation

---

# Key Takeaways

- `if` introduces decision making.
- Conditions must evaluate to `True` or `False`.
- Indentation defines the code block.
- `if` statements are used throughout AI and software engineering.

---

# Interview Questions

1. What is control flow?
2. What is an `if` statement?
3. Why is indentation important?
4. What happens when an `if` condition is `False`?
5. What is the difference between `=` and `==`?

---

# Assignment

## Practical

- Write programs using `if`.
- Practice different conditions.
- Observe how the program behaves when conditions are true and false.

## Theory

1. Explain control flow.
2. Explain the syntax of `if`.
3. Why is indentation mandatory in Python?

---

# Summary

- `if` enables programs to make decisions.
- Conditions produce Boolean values.
- Python relies on indentation instead of braces.
- `if` statements are fundamental to AI, automation, and application development.