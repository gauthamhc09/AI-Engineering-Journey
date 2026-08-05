# Chapter 12 - `if-else`

## 🎯 Learning Objectives

By the end of this chapter, you will:

- Understand the `if-else` statement
- Write programs with two possible outcomes
- Understand execution flow
- Apply `if-else` to real-world problems

---

# What is `if-else`?

An `if-else` statement allows a program to choose between two paths.

Syntax:

```python
if condition:
    # Executes when condition is True
else:
    # Executes when condition is False
```

Only one block executes.

---

# Execution Flow

```
Condition

↓

True?

↙           ↘

YES          NO

↓            ↓

if Block    else Block

↓

Continue Program
```

---

# Example

```python
age = 20

if age >= 18:
    print("Eligible to Vote")
else:
    print("Not Eligible to Vote")
```

---

# Real-World Examples

- ATM withdrawal
- Login system
- Voting eligibility
- Student results
- Password validation

---

# AI Connection

AI systems often classify predictions using thresholds.

```python
if confidence >= 0.90:
    print("High Confidence")
else:
    print("Low Confidence")
```

---

# Common Mistakes

- Using `=` instead of `==`
- Incorrect indentation
- Missing colon (`:`)

---

# Key Takeaways

- `if-else` provides two possible execution paths.
- Only one block executes.
- Conditions evaluate to `True` or `False`.
- Indentation defines code blocks.

---

# Interview Questions

1. What is `if-else`?
2. How is it different from `if`?
3. Can both blocks execute?
4. Why is indentation required?

---

# Assignment

## Practical

- Voting eligibility
- Even/Odd
- Student Result
- ATM Balance
- Password Validation

## Theory

1. Explain the execution flow of `if-else`.
2. Why can only one block execute?

---

# Summary

- `if-else` allows a program to choose between two outcomes.
- Python evaluates the condition first.
- The `if` block runs when the condition is `True`.
- The `else` block runs when the condition is `False`.