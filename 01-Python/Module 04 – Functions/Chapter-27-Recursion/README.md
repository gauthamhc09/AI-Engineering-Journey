# Chapter 27 – Recursion

## What is Recursion?

Recursion is a programming technique where a function calls itself to solve a smaller version of the same problem.

## Components of Recursion

Every recursive solution should have:

1. Base Case
2. Recursive Case

### Base Case

The condition that stops recursion.

### Recursive Case

The part where the function calls itself with a smaller or simpler problem.

## Example Structure

```python
def recursive_function(n):
    if base_condition:
        return

    recursive_function(smaller_problem)
```

## Python Internals

Every recursive function call creates a new function frame.

Example:

```text
recursive_function(3)
        ↓
recursive_function(2)
        ↓
recursive_function(1)
        ↓
recursive_function(0)
```

Each frame contains its own local variables.

When the base case is reached, the calls return in reverse order.

This process is called stack unwinding.

## Call Stack

The call stack follows LIFO:

Last In, First Out.

The most recently created function frame returns first.

## Recursion vs Iteration

Iteration uses loops:

```python
for i in range(...):
    ...
```

Recursion uses function calls:

```python
function(...)
```

Recursion is useful when a problem naturally contains nested or recursive structures.

## Common Recursive Problems

- Factorial
- Tree traversal
- File-system traversal
- Searching
- Parsing nested structures
- Divide-and-conquer algorithms

## AI Connection

Recursion can appear in:

- Tree-based search
- Decision trees
- Hierarchical data
- Abstract Syntax Trees
- Nested document processing
- Search/planning algorithms

## Common Mistakes

- Missing base case
- Base case never reached
- Moving away from the base case
- Forgetting to return recursive results
- Using recursion when iteration is simpler

## Best Practices

Before writing recursive code, identify:

1. Base case
2. Recursive case
3. Progress toward termination
4. Return behavior during stack unwinding
5. Whether recursion is actually appropriate

## Summary

Recursion allows a function to solve a problem by solving a smaller version of the same problem. Each recursive call creates a new stack frame, and once the base case is reached, the call stack unwinds in reverse order.