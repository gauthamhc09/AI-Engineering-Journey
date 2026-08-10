# Chapter 22 – Introduction to Functions

## What is a Function?

A function is a named, reusable block of code that performs a specific task. It helps organize programs into smaller, manageable pieces.

## Why Functions?

- Reduce code duplication
- Improve readability
- Simplify debugging
- Encourage code reuse
- Make testing easier
- Improve maintainability

## Function Syntax

```python
def greet():
    print("Hello")

greet()
```

## Function Lifecycle

1. Python reads the function definition.
2. A function object is created in memory.
3. The function body is **not** executed immediately.
4. When the function is called, Python creates a new function frame.
5. The function executes.
6. Control returns to the caller.

## Python Internals

- Functions are first-class objects.
- Calling a function creates a new execution frame.
- Python uses a call stack (LIFO) to manage nested function calls.
- Execution returns to the exact point after the function call.

## Real-World Usage

- Backend services
- REST APIs
- FastAPI endpoints
- Database operations
- Automation scripts
- Production applications

## AI Connection

Functions organize AI pipelines:

- Load data
- Tokenize text
- Generate embeddings
- Retrieve context
- Build prompts
- Generate model responses

## Best Practices

- Use descriptive `snake_case` names.
- Keep functions focused on one responsibility.
- Avoid duplicate code.
- Write readable, maintainable code.

## Common Mistakes

- Defining without calling
- Calling before definition
- Forgetting parentheses
- Incorrect indentation
- Creating overly large functions

## Interview Questions

### Beginner

- What is a function?
- Why do we use functions?
- Difference between defining and calling?

### Intermediate

- What happens internally during a function call?
- What is a function frame?
- What is the call stack?

## Assignments

### Basic

- Create `welcome()`
- Create `divider()`
- Call both multiple times

### Intermediate

Build a Student Report application using separate functions.

### Challenge

Build a Restaurant Menu application using multiple functions.

## Summary

Functions are one of the most important abstractions in Python. They improve organization, readability, reuse, testing, and scalability. Modern backend systems, AI frameworks, and production software are fundamentally built from functions working together.

## Important

Python executes the def statement itself, creating a function object in memory and binding it to the function's name. The statements inside the function body are not executed until the function is called.