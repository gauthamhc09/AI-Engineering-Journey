# Chapter 08 - Strings

## 🎯 Learning Objectives

By the end of this chapter, you will be able to:

- Understand strings and their importance
- Use indexing and slicing
- Work with common string methods
- Understand string immutability
- Apply strings in AI applications

---

# What is a String?

A string is a sequence of characters.

Examples:

```python
name = "Gautham"
city = "Bangalore"
message = "Hello World"
```

Strings can contain letters, numbers, spaces, symbols, and emojis.

---

# Creating Strings

```python
name = "Python"

city = 'Bangalore'

message = """
Welcome
to
Python
"""
```

---

# Indexing

Each character has a position.

```
P  y  t  h  o  n
0  1  2  3  4  5
```

Negative indexing:

```
P  y  t  h  o  n
-6 -5 -4 -3 -2 -1
```

Examples:

```python
language[0]
language[-1]
```

---

# String Length

Use:

```python
len(language)
```

---

# Slicing

Syntax:

```python
string[start:end]
```

Examples:

```python
language[0:2]
language[:4]
language[3:]
language[::-1]
```

---

# String Immutability

Strings cannot be modified after creation.

Incorrect:

```python
text[0] = "J"
```

Correct:

```python
text = "Jython"
```

---

# Common String Methods

```python
upper()
lower()
title()
capitalize()
strip()
replace()
find()
count()
```

Examples:

```python
text.upper()

text.replace("Java", "Python")

text.strip()
```

---

# Escape Characters

Examples:

```python
"I\'m Gautham"

"Hello\nWorld"

"Hello\tWorld"
```

---

# AI Connection

Every LLM interaction begins with a string.

```
User Input

↓

String

↓

Tokenizer

↓

Tokens

↓

LLM

↓

String Output
```

Prompts and responses are strings.

---

# Key Takeaways

- Strings are sequences of characters.
- Indexing accesses individual characters.
- Slicing extracts portions of strings.
- Strings are immutable.
- Python provides many built-in string methods.
- Strings are fundamental to prompt engineering and LLMs.

---

# Interview Questions

1. What is a string?
2. Explain indexing and slicing.
3. What is string immutability?
4. How do you reverse a string?
5. Name common string methods.
6. Why are strings important in AI?

---

# Assignment

## Practical

- Practice indexing and slicing.
- Reverse a string.
- Use all common string methods.
- Build small examples using `replace()`, `find()`, and `count()`.

## Theory

1. Explain string immutability.
2. Explain negative indexing.
3. Why are strings important in AI?

---

# Summary

- Strings represent text.
- Characters are accessed using indexes.
- Slicing extracts parts of strings.
- Strings are immutable.
- String methods simplify text processing.
- LLMs process strings before converting them into tokens.