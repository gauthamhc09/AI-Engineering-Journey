# Chapter 06 - Operators

## 🎯 Learning Objectives

By the end of this chapter, you will be able to:

- Understand Python operators
- Perform arithmetic calculations
- Compare values
- Combine conditions using logical operators
- Use identity and membership operators
- Understand operator precedence
- Apply operators in AI programs

---

# What is an Operator?

An operator is a symbol that performs an operation on one or more values.

Example:

```python
10 + 5
```

Here:

- `10` → Operand
- `+` → Operator
- `5` → Operand

---

# Types of Operators

- Arithmetic
- Assignment
- Comparison
- Logical
- Identity
- Membership
- Bitwise (covered later)

---

# Arithmetic Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `+` | Addition | `10 + 5` |
| `-` | Subtraction | `10 - 5` |
| `*` | Multiplication | `10 * 5` |
| `/` | Division | `10 / 5` |
| `//` | Floor Division | `10 // 3` |
| `%` | Modulus | `10 % 3` |
| `**` | Exponent | `2 ** 3` |

---

# Assignment Operators

Assign values to variables.

Examples:

```python
x = 10
x += 5
x -= 2
x *= 3
x /= 2
```

---

# Comparison Operators

Return either `True` or `False`.

| Operator | Meaning |
|----------|---------|
| `==` | Equal |
| `!=` | Not Equal |
| `>` | Greater Than |
| `<` | Less Than |
| `>=` | Greater Than or Equal |
| `<=` | Less Than or Equal |

---

# Logical Operators

| Operator | Meaning |
|----------|---------|
| `and` | Both conditions must be True |
| `or` | At least one condition must be True |
| `not` | Reverses the Boolean value |

---

# Identity Operators

Compare object identity.

| Operator | Meaning |
|----------|---------|
| `is` | Same object |
| `is not` | Different objects |

Example:

```python
x = None

print(x is None)
```

---

# Membership Operators

Check whether a value exists in a collection.

| Operator | Meaning |
|----------|---------|
| `in` | Exists |
| `not in` | Does not exist |

Example:

```python
print("AI" in "OpenAI")
```

---

# Operator Precedence

Python evaluates operators according to precedence.

```python
print(2 + 3 * 4)
```

Output:

```
14
```

Use parentheses to change the order:

```python
print((2 + 3) * 4)
```

Output:

```
20
```

---

# AI Connection

Operators are widely used in AI.

Examples:

```python
confidence >= 0.90

epoch == 100

gpu_available and internet

token in vocabulary
```

---

# Key Takeaways

- Operators perform actions on values.
- Arithmetic operators perform calculations.
- Comparison operators return Boolean values.
- Logical operators combine conditions.
- Identity operators compare object identity.
- Membership operators check for presence.
- Parentheses improve readability and control precedence.

---

# Interview Questions

1. What is an operator?
2. What is the difference between `=` and `==`?
3. Explain `/` vs `//`.
4. What is the purpose of `%`?
5. What is the difference between `==` and `is`?
6. What are logical operators?
7. Explain operator precedence.

---

# Assignment

## Practical

- Practice every operator with examples.
- Observe the output of each operation.
- Experiment with operator precedence.

## Theory

1. Explain each category of operators.
2. Why are comparison operators important?
3. Where are operators used in AI applications?

---

# Summary

- Operators are fundamental building blocks of Python.
- They perform calculations, comparisons, logical decisions, identity checks, and membership tests.
- Understanding operators is essential before learning control flow (`if` statements).
- AI and machine learning code relies heavily on operators for decision making and computations.