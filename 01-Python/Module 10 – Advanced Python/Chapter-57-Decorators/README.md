# Chapter 57 — Decorators

## 1. What is a Decorator?

A **decorator** is a function that takes another function, extends or modifies its behavior, and returns a function.

Core idea:

```text
Original function
      ↓
   Decorator
      ↓
    Wrapper
      ↓
Extra behavior + original function
```

Common uses:
- Logging
- Authentication
- Authorization
- Validation
- Timing
- Caching
- Retries

---

## 2. Functions Are First-Class Objects

Python functions can be assigned to variables, passed as arguments, and returned from other functions.

```python
def greet():
    print("Hello")

def execute(function):
    function()

execute(greet)
```

A function can also return another function:

```python
def outer():
    def inner():
        print("Hello")
    return inner
```

---

## 3. Basic Decorator

```python
def my_decorator(func):

    def wrapper():
        print("Before function")
        func()
        print("After function")

    return wrapper
```

Manual decoration:

```python
greet = my_decorator(greet)
```

The decorator receives the original function and returns the wrapper.

---

## 4. `@decorator` Syntax

```python
@my_decorator
def greet():
    print("Hello")
```

is approximately equivalent to:

```python
def greet():
    print("Hello")

greet = my_decorator(greet)
```

Mental model:

```python
@decorator
def function():
```

means:

```python
function = decorator(function)
```

---

## 5. Wrapper Function

The wrapper surrounds the original function:

```text
wrapper()
   ↓
Before
   ↓
original function
   ↓
After
```

This lets a decorator add behavior before and/or after the original function.

---

## 6. Decorators with Arguments

A wrapper should generally support arbitrary arguments:

```python
def decorator(func):

    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper
```

- `*args` captures positional arguments.
- `**kwargs` captures keyword arguments.

This makes the decorator more generic.

---

## 7. Preserving Return Values

If the original function returns a value, preserve it:

```python
def decorator(func):

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result

    return wrapper
```

Otherwise the decorated function may unexpectedly return `None`.

---

## 8. Example — Uppercase Decorator

```python
def uppercase_decorator(func):

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()

    return wrapper


@uppercase_decorator
def greet(name):
    return f"hello {name}"

print(greet("Angel"))
```

Output:

```text
HELLO ANGEL
```

Flow:

```text
greet("Angel")
      ↓
wrapper("Angel")
      ↓
original greet("Angel")
      ↓
"hello Angel"
      ↓
.upper()
      ↓
"HELLO ANGEL"
```

---

## 9. `functools.wraps`

Without `wraps`:

```python
print(greet.__name__)
```

may produce:

```text
wrapper
```

because `greet` now refers to the wrapper.

Use:

```python
from functools import wraps

def uppercase_decorator(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()

    return wrapper
```

Now the original metadata is preserved:

```python
@uppercase_decorator
def greet(name):
    """Greets a person."""
    return f"hello {name}"

print(greet.__name__)
print(greet.__doc__)
```

Output:

```text
greet
Greets a person.
```

`@wraps(func)` preserves important metadata such as:
- `__name__`
- `__doc__`
- `__module__`
- `__annotations__`

Mental model:

> `@wraps(func)` tells Python that the wrapper represents the original function.

---

## 10. Decorator Factories

Sometimes we want to pass configuration:

```python
@repeat(3)
def greet():
    print("Hello")
```

`repeat(3)` must execute first and return a decorator.

Structure:

```text
repeat(3)
    ↓
 decorator
    ↓
  wrapper
    ↓
original function
```

Example:

```python
def repeat(times):

    def decorator(func):

        def wrapper():

            for _ in range(times):
                func()

        return wrapper

    return decorator
```

Usage:

```python
@repeat(3)
def greet():
    print("Hello")

greet()
```

Output:

```text
Hello
Hello
Hello
```

Generic version:

```python
from functools import wraps

def repeat(times):

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            for _ in range(times):
                func(*args, **kwargs)

        return wrapper

    return decorator
```

Usage:

```python
@repeat(3)
def greet(name):
    print(f"Hello {name}")

greet("Angel")
```

---

## 11. Multiple Decorators

```python
@first
@second
def hello():
    print("Hello")
```

is equivalent to:

```python
hello = first(second(hello))
```

### Application order

Decorators are **applied from bottom to top**.

`second` wraps `hello` first, then `first` wraps the result.

### Execution order

When `hello()` is called, execution starts with the **outermost wrapper**:

```text
first wrapper
     ↓
second wrapper
     ↓
original hello
```

Example:

```python
def first(func):

    def wrapper():
        print("First before")
        func()
        print("First after")

    return wrapper


def second(func):

    def wrapper():
        print("Second before")
        func()
        print("Second after")

    return wrapper


@first
@second
def hello():
    print("Hello")

hello()
```

Output:

```text
First before
Second before
Hello
Second after
First after
```

Mental model:

```text
first(second(hello))
```

Execution:

```text
First before
    ↓
Second before
    ↓
Hello
    ↑
Second after
    ↑
First after
```

---

## 12. Decorators in Real Applications

Decorators are heavily used in Python frameworks.

For example, FastAPI uses decorator syntax:

```python
@app.get("/users")
def get_users():
    return {"users": []}
```

Conceptually:

```python
get_users = app.get("/users")(get_users)
```

Decorators are useful for cross-cutting concerns such as:
- Authentication
- Authorization
- Logging
- Validation
- Timing
- Caching
- Error handling

---

## 13. Key Mental Models

### Basic decorator

```python
@decorator
def func():
```

approximately means:

```python
func = decorator(func)
```

### Decorator factory

```python
@repeat(3)
def func():
```

approximately means:

```python
func = repeat(3)(func)
```

### Multiple decorators

```python
@A
@B
def func():
```

means:

```python
func = A(B(func))
```

### Three-layer decorator factory

```text
configuration
     ↓
decorator
     ↓
wrapper
     ↓
original function
```

---

## 14. Important Terms

| Term | Meaning |
|---|---|
| Decorator | Function that modifies or extends another function |
| Wrapper | Inner function that surrounds the original function |
| `@decorator` | Syntax for applying a decorator |
| `*args` | Captures positional arguments |
| `**kwargs` | Captures keyword arguments |
| `wraps` | Preserves original function metadata |
| Decorator factory | Function that accepts configuration and returns a decorator |
| Nested decorators | Multiple decorators applied to one function |

---

## Chapter Summary

A decorator wraps a function to add behavior without directly modifying the original function.

The fundamental pattern is:

```python
def decorator(func):

    def wrapper(*args, **kwargs):
        # extra behavior
        result = func(*args, **kwargs)
        # more behavior
        return result

    return wrapper
```

Use `@wraps(func)` to preserve the original function's metadata.

For configurable decorators such as `@repeat(3)`, use a decorator factory:

```text
repeat(3)
   ↓
decorator
   ↓
wrapper
   ↓
function
```

For multiple decorators:

```python
@A
@B
def func():
```

remember:

```python
func = A(B(func))
```

**Core idea:**

> A decorator wraps a function, intercepts its call, can perform additional work before and after it, and can return or modify its result.
