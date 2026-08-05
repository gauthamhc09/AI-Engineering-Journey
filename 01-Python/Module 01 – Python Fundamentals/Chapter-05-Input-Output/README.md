# Chapter 05 - Input & Output

## 🎯 Learning Objectives

By the end of this chapter, you will be able to:

- Understand the IPO (Input → Process → Output) model
- Use the `print()` function effectively
- Accept user input with `input()`
- Convert input into different data types
- Format output using f-strings
- Understand how input and output are used in AI applications

---

# The IPO Model

Every program follows the same basic flow:

```
Input
  ↓
Process
  ↓
Output
```

Examples:

- Calculator
- ATM
- ChatGPT
- Banking System
- AI Chatbot

---

# Output with `print()`

The `print()` function displays information on the screen.

Example:

```python
print("Hello World")
```

You can print:

- Strings
- Integers
- Floats
- Booleans
- Variables

---

# Printing Variables

```python
name = "Gautham"

print(name)
```

---

# Printing Multiple Values

```python
name = "Gautham"
age = 33

print(name, age)
```

Output:

```
Gautham 33
```

---

# `sep` Parameter

Changes the separator between printed values.

```python
print("Python", "AI", "Engineer", sep="-")
```

Output:

```
Python-AI-Engineer
```

---

# `end` Parameter

Changes what `print()` appends at the end.

```python
print("Hello", end=" ")
print("World")
```

Output:

```
Hello World
```

---

# Input with `input()`

The `input()` function accepts user input.

```python
name = input("Enter your name: ")
```

---

# Important Note

`input()` **always returns a string**.

Example:

```python
age = input("Enter age: ")

print(type(age))
```

Output:

```
<class 'str'>
```

---

# Type Conversion

Convert input when numeric operations are required.

```python
age = int(input("Enter age: "))
```

Common conversions:

```python
int()
float()
str()
bool()
```

---

# f-Strings

The preferred way to format output.

```python
name = "Gautham"

print(f"Hello {name}")
```

Output:

```
Hello Gautham
```

---

# AI Connection

AI applications use the same concepts.

```python
prompt = input("Ask something: ")

response = model(prompt)
```

The prompt is user input, and the model generates the output.

---

# Key Takeaways

- Every program follows the IPO model.
- `print()` displays output.
- `input()` collects user input.
- `input()` always returns a string.
- Use type conversion when necessary.
- Prefer f-strings for formatting output.

---

# Interview Questions

1. What is the IPO model?
2. What does `input()` return?
3. Why do we use `int(input())`?
4. What are f-strings?
5. Explain the difference between `sep` and `end`.

---

# Assignment

## Practical

- Create greeting, age, and calculator programs.
- Practice `sep`, `end`, and f-strings.

## Theory

1. Explain the IPO model.
2. Why does `input()` return a string?
3. Why are f-strings preferred?
4. How are input and output used in AI applications?

---

# Summary

- Programs receive input, process it, and produce output.
- `print()` and `input()` are two of Python's most important built-in functions.
- Type conversion allows us to work with numeric input.
- f-strings provide clean and readable output formatting.
- Input and output are fundamental concepts in every AI application.