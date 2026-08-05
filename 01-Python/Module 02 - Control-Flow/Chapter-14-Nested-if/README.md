# Chapter 14 - Nested `if`

## 🎯 Learning Objectives

By the end of this chapter, you will:

- Understand nested `if`
- Write decision trees with multiple conditions
- Compare nested `if` with logical operators
- Apply nested `if` in real-world applications

---

# What is a Nested `if`?

A nested `if` is an `if` statement inside another `if` statement.

Syntax:

```python
if condition1:
    if condition2:
        print("Executed")
```

The inner condition is evaluated only if the outer condition is `True`.

---

# Execution Flow

```
Condition 1

↓

True?

↓

YES

↓

Condition 2

↓

True?

↓

Execute Block
```

If the outer condition is `False`, the inner condition is never checked.

---

# Real-World Examples

- ATM systems
- Login authentication
- Scholarship eligibility
- API validation
- Shopping checkout

---

# Nested `if` vs `and`

Nested `if`:

```python
if balance >= withdraw:
    if pin == "1234":
        print("Success")
```

Logical operator:

```python
if balance >= withdraw and pin == "1234":
    print("Success")
```

Nested `if` is useful when later checks depend on earlier ones.

---

# AI Connection

AI systems often validate one step before moving to the next.

Example:

```python
if api_key == "VALID":
    prompt = input("Enter Prompt: ")

    if len(prompt) >= 10:
        print("Processing")
```

---

# Common Mistakes

- Incorrect indentation
- Excessive nesting
- Using nested `if` where simpler logic would work

---

# Key Takeaways

- Nested `if` allows decisions inside decisions.
- Inner blocks execute only if outer conditions succeed.
- Keep nesting readable.
- Use nested `if` when later steps depend on earlier validation.

---

# Interview Questions

1. What is a nested `if`?
2. When should you use nested `if`?
3. How is it different from using `and`?
4. What are the drawbacks of deep nesting?

---

# Assignment

## Practical

- ATM System
- Login System
- Scholarship Checker
- Shopping Checkout

## Theory

1. Explain nested `if`.
2. Compare nested `if` with logical operators.
3. Where are nested `if` statements used?

---

# Summary

- Nested `if` represents multi-stage decision making.
- Each inner condition depends on the outer condition.
- They are commonly used in authentication, banking, and AI workflows.