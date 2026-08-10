# Chapter 25 – Variable Scope

## What is Scope?

Scope defines where a variable is visible and can be accessed in a program.

## Types of Scope (Current Chapter)

- Global Scope
- Local Scope

## Global Variable

Declared outside all functions.

```python
name = "Gautham"
```

Accessible from functions unless shadowed by a local variable.

## Local Variable

Declared inside a function.

```python
def greet():
    message = "Hello"
```

Exists only while the function executes.

## Python Internals

- The program starts with a Global Frame.
- Every function call creates a new Function Frame.
- Local variables live inside their function frame.
- When the function returns, its frame is destroyed and local variables disappear.

## Variable Shadowing

A local variable with the same name as a global variable temporarily hides the global variable inside the function.

## AI Connection

AI pipelines often use:

- Global configuration (`MODEL_NAME`, `API_KEY`)
- Local processing variables (`tokens`, `embeddings`, `response`)

Returned values move information from local scope back to the caller.

## Best Practices

- Prefer local variables.
- Minimize global state.
- Return values instead of modifying globals.
- Use clear variable names.

## Common Mistakes

- Accessing local variables outside a function.
- Expecting local variables to persist after the function returns.
- Confusing shadowing with modifying a global variable.

## Summary

Variable scope determines where variables exist and how long they live. Understanding scope is essential for writing predictable, maintainable Python code and is foundational for backend development and AI systems.