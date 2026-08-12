# Chapter 23 – Function Parameters

## What are Functions with Parameters?

A parameter allows a function to receive input values, making it reusable for different data.

## Parameter vs Argument

```python
def greet(name):
    print(name)

greet("Gautham")
```

- `name` → Parameter
- `"Gautham"` → Argument

## Execution Flow

1. Function object is created.
2. Function is called with arguments.
3. Python creates a new function frame.
4. Arguments are bound to parameters.
5. Function body executes.
6. Function frame is destroyed after execution.

## Python Internals

- Parameters become local variables inside the function frame.
- Each function call gets a new frame.
- Parameter values exist only during that function call.

## AI Connection

Parameters are fundamental to AI systems:

- `tokenizer(text)`
- `model.generate(prompt)`
- `create_embedding(text)`
- `predict(image)`

These functions process different inputs using the same logic.

## Best Practices

- Use descriptive parameter names.
- Keep functions focused.
- Avoid excessive numbers of parameters.
- Write reusable functions.

## Common Mistakes

- Forgetting required arguments
- Passing the wrong number of arguments
- Confusing parameters with arguments
- Using undefined variables inside functions

## Summary

Parameters transform functions from fixed procedures into reusable building blocks that can operate on different inputs. They are a foundational concept used throughout Python, web development, and AI engineering.