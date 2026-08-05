# Chapter 02 - Installing Python & Understanding How Python Works

## 🎯 Learning Objectives

By the end of this chapter, you will be able to:

- Install Python correctly
- Understand how Python executes a program
- Explain the role of the Python Interpreter
- Understand Bytecode and the Python Virtual Machine (PVM)
- Differentiate between Compiled and Interpreted languages
- Run Python programs using VS Code and the Terminal
- Understand why Python is the most popular language for AI

---

# Why Do We Need Programming Languages?

Computers only understand **Machine Language (Binary)**.

Example:

010101010100101010101...

Humans cannot efficiently write programs in binary.

Programming languages act as a bridge between humans and computers.

```
Human
    ↓
Programming Language (Python)
    ↓
Machine Language
    ↓
Computer
```

Python allows us to write instructions in a way that is easy for humans to understand.

Example:

```python
print("Hello World")
```

instead of writing binary instructions.

---

# Evolution of Programming Languages

Programming languages have evolved to become more readable and productive.

```
Machine Language
        ↓
Assembly Language
        ↓
C
        ↓
C++
        ↓
Java
        ↓
Python
```

Each generation improved developer productivity and readability.

---

# Why Python?

Python is designed to be:

- Simple
- Readable
- Beginner Friendly
- Powerful
- Cross Platform

Python is widely used in:

- Artificial Intelligence
- Machine Learning
- Data Science
- Automation
- Web Development
- Cyber Security
- Cloud Computing

---

# Python vs Other Languages

### C

```c
#include <stdio.h>

int main()
{
    printf("Hello");
    return 0;
}
```

### Java

```java
class Main{
    public static void main(String args[]){
        System.out.println("Hello");
    }
}
```

### Python

```python
print("Hello")
```

Python requires significantly less code while remaining highly readable.

---

# What Happens When We Run a Python Program?

When we write Python code, the computer cannot understand it directly.

Python uses an Interpreter to execute our code.

Execution flow:

```
Python Source Code (.py)

        ↓

Python Interpreter

        ↓

Bytecode

        ↓

Python Virtual Machine (PVM)

        ↓

Machine Code

        ↓

CPU

        ↓

Output
```

---

# Step 1 – Source Code

The code written by the programmer is called **Source Code**.

Example:

```python
print("Hello AI")
```

Python files have the extension:

```
.py
```

Examples:

```
main.py
chatbot.py
hello.py
```

---

# Step 2 – Python Interpreter

The Python Interpreter is a software program that executes Python code.

Responsibilities:

- Reads Python source code
- Checks for syntax errors
- Converts source code into Bytecode
- Executes the program

Real-world analogy:

Imagine speaking English to someone who only understands Japanese.

A translator converts your English into Japanese.

Similarly,

```
You
    ↓
Python Interpreter
    ↓
Computer
```

The Interpreter acts as the translator between humans and computers.

---

# Step 3 – Bytecode

Python first converts source code into **Bytecode**.

Bytecode is:

- Intermediate code
- Platform Independent
- Generated automatically
- Not directly readable by humans

Developers normally do not interact with Bytecode directly.

---

# Step 4 – Python Virtual Machine (PVM)

The Python Virtual Machine (PVM) executes the Bytecode.

Flow:

```
Python Code

↓

Bytecode

↓

Python Virtual Machine

↓

Machine Code

↓

CPU
```

The PVM is responsible for running Python programs.

---

# Why is Python Slower than C?

### C Execution

```
C Source Code

↓

Compiler

↓

Machine Code

↓

CPU
```

### Python Execution

```
Python Source Code

↓

Interpreter

↓

Bytecode

↓

Python Virtual Machine

↓

CPU
```

Python has additional execution steps, making it slower than compiled languages like C.

---

# Why Do AI Engineers Still Use Python?

Although Python itself is slower than C, most AI libraries are implemented using highly optimized C/C++ and CUDA code.

Examples:

- NumPy
- PyTorch
- TensorFlow
- OpenCV

When we write:

```python
import torch
```

Python acts as an easy-to-use interface while the heavy computations are performed by optimized native code.

This combination provides both developer productivity and high performance.

---

# Compiled vs Interpreted Languages

| Compiled Languages | Python |
|--------------------|---------|
| Source → Machine Code | Source → Bytecode → PVM |
| Generates executable files | Requires Python Runtime |
| Faster execution | Slightly slower execution |
| Example: C | Example: Python |

Note:

Python is commonly called an **interpreted language**, but internally CPython first compiles source code into Bytecode before executing it using the Python Virtual Machine.

---

# Running Python from Terminal

Check Python version:

```bash
python --version
```

or

```bash
python3 --version
```

Example Output:

```text
Python 3.13.2
```

---

# Creating Your First Python Program

Create a file:

```
hello.py
```

Example:

```python
print("Hello Gautham!")

print("Welcome to Python!")

print("Future AI Engineer!")
```

Run the program using:

- VS Code
- Terminal

---

# AI Connection

Every AI application begins with Python.

Example:

```python
from transformers import pipeline
```

Later we can write:

```python
classifier = pipeline("sentiment-analysis")

result = classifier("Python is amazing!")
```

Although we are using AI libraries, we are still writing Python code.

Python is the foundation of AI Engineering.

---

# Key Takeaways

- Computers understand only Machine Language.
- Python is a high-level programming language.
- Python programs are executed using the Python Interpreter.
- Source code is converted into Bytecode.
- Bytecode is executed by the Python Virtual Machine.
- Python is slower than C because it has additional execution steps.
- Python remains the preferred language for AI because of its simplicity and rich ecosystem.

---

# Interview Questions

### 1. What is Python?

### 2. Why is Python popular?

### 3. What is the Python Interpreter?

### 4. What is Bytecode?

### 5. What is the Python Virtual Machine?

### 6. Explain the execution flow of a Python program.

### 7. Why is Python slower than C?

### 8. Why is Python the most popular language for AI?

---

# Assignment

## Practical

- Install Python
- Install VS Code
- Create `hello.py`
- Run the program using VS Code
- Run the same program using Terminal

## Theory

Write answers in your own words:

1. Why do we need programming languages?
2. What is the Python Interpreter?
3. What is Bytecode?
4. What is the Python Virtual Machine?
5. Why is Python used for AI?

---

# Summary

- Programming languages allow humans to communicate with computers.
- Python emphasizes readability and simplicity.
- Python code is first converted into Bytecode.
- The Python Virtual Machine executes Bytecode.
- Python is slower than C but much easier to develop with.
- AI engineers use Python because it combines simplicity with a powerful ecosystem.