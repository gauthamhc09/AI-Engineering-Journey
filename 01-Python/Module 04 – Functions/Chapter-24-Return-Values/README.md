# Chapter 24 – The `return` Statement

## What is `return`?

The `return` statement ends a function and sends a value back to the caller.

## `print()` vs `return`

| print() | return |
|----------|---------|
| Displays output | Returns a value |
| Used for users | Used by other code |
| Doesn't transfer data | Transfers data |

## Execution Flow

1. Function is called.
2. Python creates a function frame.
3. Statements execute.
4. `return` evaluates its expression.
5. Function frame is destroyed.
6. Returned value is handed to the caller.

## Python Internals

- `return` immediately stops function execution.
- Local variables are destroyed when the function frame ends.
- The returned value is passed back before the frame is removed.

## AI Connection

Most AI libraries return objects:

- Tokens
- Embeddings
- Predictions
- Responses
- Tensors

These returned values become inputs to later stages of an AI pipeline.

## Best Practices

- Prefer returning values over printing.
- Keep computation separate from presentation.
- Use descriptive function names.

## Common Mistakes

- Using `print()` instead of `return`
- Writing unreachable code after `return`
- Forgetting to use the returned value

## Summary

The `return` statement transforms functions from simple procedures into reusable computational units. It enables composition, testing, and data flow throughout modern Python applications and AI systems.