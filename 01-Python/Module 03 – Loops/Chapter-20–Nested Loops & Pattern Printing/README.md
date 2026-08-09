# Chapter 20 – Nested Loops & Pattern Printing

## What is a Nested Loop?

A nested loop is a loop inside another loop.

```python
for row in range(rows):
    for column in range(columns):
        # work
```

## Key Concepts

- Outer loop controls rows.
- Inner loop controls columns.
- The inner loop restarts for every outer-loop iteration.

## `print(end=" ")`

By default:

```python
print("Hello")
```

uses `end="\n"`.

Using:

```python
print("*", end=" ")
```

keeps printing on the same line.

A standalone `print()` moves to the next line.

## Real Applications

- Excel spreadsheets
- Image processing
- Matrices
- Chess boards
- Tables
- Neural network tensors
- Dataset processing

## AI Connection

Nested loops help build intuition for:

- Images (rows × columns)
- Matrices
- Attention matrices
- Batch → Sample processing
- Grid-based algorithms

## Common Mistakes

- Forgetting `print()` after the inner loop.
- Incorrect indentation.
- Assuming the inner loop remembers its previous state.

## Best Practices

- Use `row` and `column` as variable names.
- Keep nesting shallow when possible.
- Separate row logic from column logic.

## Interview Questions

1. What is a nested loop?
2. Why does the inner loop restart?
3. Why is `end=" "` used?
4. How many times does a nested loop execute?

## Assignments

- 4×4 square
- 5×3 rectangle
- Right triangle
- Inverted triangle
- Number triangle
- Multiplication table