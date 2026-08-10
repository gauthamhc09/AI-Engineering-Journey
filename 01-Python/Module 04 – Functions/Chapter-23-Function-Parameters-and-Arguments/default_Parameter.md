# Default Parameters

## What are Default Parameters?

Default parameters allow a function to provide a predefined value when the caller does not supply one.

## Syntax

```python
def greet(name="Guest"):
    print(f"Hello {name}")
```

## How It Works

- If no argument is passed, Python uses the default value.
- If an argument is provided, it overrides the default.

## Python Internals

- Default values are stored in the function object when the `def` statement executes.
- During a function call, Python binds either the provided argument or the stored default to the parameter.
- Each function call still creates a new function frame.

## Real-World Uses

- File handling: `open(file, mode="r")`
- FastAPI query parameters
- AI model settings like `temperature` and `max_tokens`
- Logging utilities

## Best Practices

- Put required parameters before optional ones.
- Use meaningful defaults.
- Avoid mutable default values.

## Common Mistakes

- Placing required parameters after default parameters.
- Assuming defaults are always used.
- Using mutable objects as defaults.

## Summary

Default parameters make functions flexible by allowing optional inputs while keeping a single reusable function.