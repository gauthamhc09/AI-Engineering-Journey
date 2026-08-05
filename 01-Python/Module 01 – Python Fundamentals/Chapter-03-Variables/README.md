# Chapter 03 - Variables & Memory

## 🎯 Learning Objectives

By the end of this chapter, you will be able to:

- Understand what a variable is in Python
- Learn how variables reference objects in memory
- Create and use variables
- Reassign variables
- Follow Python variable naming rules
- Understand Python's dynamic typing
- Use the `type()` function
- Avoid common beginner mistakes
- Understand how variables are used in AI applications

---

# Why Do We Need Variables?

Imagine writing a program that stores your name.

Without variables:

```python
print("Gautham")
print("Gautham")
print("Gautham")
```

If your name changes (or you're storing different values), you would have to update it everywhere.

Variables solve this problem by giving a value a meaningful name.

Example:

```python
name = "Gautham"
```

Now, whenever you need the value, you use the variable instead of rewriting the data.

---

# What is a Variable?

A variable is **a name that refers to an object in memory**.

Many beginner tutorials describe a variable as a "container."

That analogy is useful initially, but Python actually works by binding names to objects.

Example:

```python
name = "Gautham"
```

Here:

- `"Gautham"` is a string object.
- `name` is a variable that refers to that object.

---

# Variables and Memory

When Python executes:

```python
name = "Gautham"
```

A string object is created in memory, and the variable `name` points to it.

```
Memory

+--------------------+
| "Gautham"          |
+--------------------+
          ▲
          │
        name
```

Variables reference objects rather than storing the data directly.

This concept becomes especially important when working with lists, dictionaries, classes, and AI models.

---

# Creating Variables

Examples:

```python
name = "Gautham"

age = 33

salary = 85000

is_engineer = True
```

Python automatically determines the data type of each value.

---

# Printing Variables

Example:

```python
name = "Gautham"

print(name)
```

Output:

```text
Gautham
```

Another example:

```python
age = 33

print(age)
```

Output:

```text
33
```

---

# Multiple Variables

```python
name = "Gautham"

age = 33

country = "India"

print(name)
print(age)
print(country)
```

Output:

```text
Gautham
33
India
```

---

# Reassigning Variables

Variables can be updated to refer to a different object.

Example:

```python
age = 33

print(age)

age = 34

print(age)
```

Output:

```text
33
34
```

The variable name remains the same, but it now points to a new value.

---

# Variable Naming Rules

A variable name:

- Can contain letters
- Can contain digits (but cannot start with one)
- Can contain underscores (`_`)
- Cannot contain spaces
- Cannot contain special characters like `-`, `@`, `#`
- Cannot use Python keywords

### Valid Variable Names

```python
name = "Gautham"

employee_name = "John"

salary2026 = 100000

_is_valid = True
```

### Invalid Variable Names

```python
2name = "John"

user-name = "John"

class = "AI"
```

---

# Variable Naming Convention

Python follows the **snake_case** naming convention.

Good:

```python
employee_name = "Gautham"

total_salary = 100000
```

Avoid:

```python
EmployeeName

employeeName

EMPLOYEENAME
```

Using meaningful variable names makes code easier to read and maintain.

---

# Dynamic Typing

Python is a dynamically typed language.

You do not need to declare the data type explicitly.

Example:

```python
age = 33

name = "Gautham"

salary = 100000.50

is_ai_engineer = False
```

Python automatically identifies the appropriate data type.

---

# Checking Data Types

The built-in `type()` function returns the type of an object.

Example:

```python
age = 33

print(type(age))
```

Output:

```text
<class 'int'>
```

More examples:

```python
print(type("Hello"))

print(type(3.14))

print(type(True))
```

Output:

```text
<class 'str'>
<class 'float'>
<class 'bool'>
```

---

# Python is Case-Sensitive

Variable names with different capitalization are different variables.

Example:

```python
name = "Gautham"

Name = "Akash"

print(name)

print(Name)
```

Output:

```text
Gautham
Akash
```

---

# Common Beginner Mistakes

## Mistake 1

```python
Name = "Gautham"

print(name)
```

❌ Error because `Name` and `name` are different variables.

---

## Mistake 2

```python
salary = 10000

print(Salary)
```

❌ Incorrect capitalization causes an error.

---

## Mistake 3

```python
user-name = "Gautham"
```

❌ Hyphens (`-`) are interpreted as the subtraction operator.

Correct:

```python
user_name = "Gautham"
```

---

# AI Connection

Variables are used everywhere in AI applications.

Example:

```python
from transformers import pipeline

model = pipeline("sentiment-analysis")

text = "I love Python"

result = model(text)
```

Here:

- `model` stores the AI model
- `text` stores the input
- `result` stores the prediction

Every AI application relies heavily on variables.

---

# Best Practices

- Use meaningful variable names.
- Follow `snake_case`.
- Avoid single-letter variable names unless appropriate (such as loop counters).
- Keep naming consistent throughout the project.

Good:

```python
employee_salary

total_marks

student_name
```

Avoid:

```python
a

x

abc

temp1
```

unless the context makes their purpose obvious.

---

# Key Takeaways

- A variable is a name that refers to an object in memory.
- Variables make programs readable and maintainable.
- Python automatically determines the data type.
- Variables can be reassigned.
- Python is case-sensitive.
- Follow the `snake_case` naming convention.
- Variables are fundamental to every Python and AI application.

---

# Interview Questions

### 1. What is a variable?

### 2. What happens internally when we write:

```python
name = "Gautham"
```

### 3. What is dynamic typing?

### 4. Why is Python called a dynamically typed language?

### 5. Explain Python variable naming rules.

### 6. Why is Python case-sensitive?

### 7. What does the `type()` function do?

---

# Assignment

## Practical

Create a file named `variables.py`.

Write a program that:

- Stores your name
- Stores your age
- Stores your city
- Stores your dream job
- Stores your favorite programming language

Print each value.

Update one variable and print it again.

Display the data type of each variable using `type()`.

---

## Theory

Write answers in your own words:

1. What is a variable?
2. Why do we need variables?
3. What is dynamic typing?
4. What are Python naming rules?
5. What are some common mistakes beginners make?

---

# Summary

- Variables provide names for values.
- Variables in Python refer to objects in memory.
- Python automatically determines object types.
- Variables can point to different objects over time.
- Good naming conventions improve code readability.
- Variables are one of the most important concepts in programming and AI development.