# Chapter 13 - `elif`

## 🎯 Learning Objectives

By the end of this chapter, you will:

- Understand the `elif` statement
- Write programs with multiple decision paths
- Learn the execution flow of `if-elif-else`
- Avoid common mistakes

---

# What is `elif`?

`elif` means **Else If**.

It allows Python to check multiple conditions.

Syntax:

```python
if condition1:
    # Code
elif condition2:
    # Code
elif condition3:
    # Code
else:
    # Code
```

---

# Execution Flow

Python evaluates conditions from top to bottom.

The first condition that is `True` executes.

The remaining conditions are skipped.

Only one block executes.

---

# Example

```python
marks = 82

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 35:
    print("Grade D")
else:
    print("Fail")
```

---

# Real-World Applications

- Student grading
- Traffic signals
- Age categorization
- User roles
- AI confidence levels

---

# AI Connection

AI models often classify confidence into ranges.

```python
if confidence >= 0.95:
    print("Excellent")
elif confidence >= 0.85:
    print("Good")
elif confidence >= 0.70:
    print("Average")
else:
    print("Low")
```

---

# Common Mistakes

- Incorrect condition order
- Using multiple `if` statements instead of `elif`
- Forgetting the `else` block

---

# Key Takeaways

- `elif` allows multiple conditions.
- Python stops after the first `True` condition.
- Order conditions from most specific to least specific.
- Only one block executes.

---

# Interview Questions

1. What is `elif`?
2. Why is condition order important?
3. Can multiple `elif` blocks execute?
4. What is the difference between multiple `if`s and `if-elif-else`?

---

# Assignment

## Practical

- Grade Calculator
- Traffic Signal
- Employee Roles
- Salary Bonus Calculator

## Theory

1. Explain `elif`.
2. Explain the execution flow.
3. Why should conditions be ordered carefully?

---

# Summary

- `elif` enables multiple decision paths.
- Python checks conditions sequentially.
- Only the first matching block executes.
- `elif` is commonly used in real-world applications and AI systems.