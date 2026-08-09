# Chapter 17 – While Loops

## What is a While Loop?

A `while` loop repeatedly executes a block of code as long as its condition evaluates to `True`.

### Syntax

```python
while condition:
    # code block
```

## Flow

1. Evaluate the condition.
2. If `True`, execute the loop body.
3. Return to the condition.
4. Repeat until the condition becomes `False`.

## Key Concepts

- Entry-controlled loop
- Condition evaluated before each iteration
- Requires updating loop variables
- Can execute zero times
- Can become an infinite loop if the condition never changes

## Example

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

## Python Internals

- The loop body exists only once in memory.
- Python re-evaluates the condition before every iteration.
- Variables are updated between iterations.
- The loop exits when the condition becomes `False`.

## AI Connection

- Training loops
- Batch processing
- Token generation
- Retry logic
- AI agents
- Streaming model responses

## Common Mistakes

- Forgetting to update variables
- Wrong loop condition
- Incorrect indentation
- Creating accidental infinite loops

## Best Practices

- Use descriptive variable names.
- Ensure the loop has a termination condition.
- Keep the loop body simple.
- Test edge cases.

## Interview Questions

1. What is a `while` loop?
2. What is an infinite loop?
3. Can a `while` loop execute zero times?
4. When would you use `while` instead of `for`?

## Assignments

### Basic

- Print 1–10
- Print 10–1
- Even numbers
- Odd numbers
- Multiplication table

### Intermediate

- Sum 1–100
- Factorial
- Reverse digits
- Count digits
- Validate positive input

### Challenge

- Fibonacci
- Palindrome
- Prime number
- Three-attempt login system

## Summary

`while` loops are ideal when the number of iterations is not known in advance. They are widely used in interactive programs, servers, AI systems, and automation tasks where execution continues until a condition changes.