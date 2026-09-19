# Chapter 58 — Context Managers

## 1. Why context managers?

Some operations need setup and cleanup: opening files, acquiring locks, or managing database sessions. If an exception interrupts the code, cleanup still needs to happen.

```python
file = open("notes.txt", "w")
try:
    file.write("Learning Python")
finally:
    file.close()
```

A `with` statement makes this lifecycle simpler:

```python
with open("notes.txt", "w") as file:
    file.write("Learning Python")
```

The file is closed when the block exits, including when an exception occurs.

## 2. Class-based context manager protocol

A class-based context manager implements:

- `__enter__()` — called when entering the `with` block.
- `__exit__(self, exc_type, exc_value, traceback)` — called when leaving it.

```python
class MyContext:
    def __enter__(self):
        print("Entering")
        return "Hello from context"

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting")

with MyContext() as value:
    print(value)
```

Output:

```text
Entering
Hello from context
Exiting
```

The value returned by `__enter__()` is assigned to the variable after `as`.

## 3. Exception handling in `__exit__`

`__exit__()` runs whether the block ends normally or because of an exception. It receives:

- `exc_type`: exception class, e.g. `ValueError`
- `exc_value`: exception instance/message
- `traceback`: traceback object

When no exception occurs, all three are `None`.

```python
class MyContext:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting")
        print(exc_type)
        print(exc_value)

with MyContext():
    raise ValueError("Something went wrong")
```

`__exit__()` runs, then the uncaught exception propagates and Python displays its traceback.

**Suppression rule:**
- Return `True` from `__exit__()` to suppress the exception.
- Return `False` or `None` to let it propagate.

Suppress exceptions only when that is intentional.

## 4. A custom class-based manager

```python
class Session:
    def __enter__(self):
        print("Opening session")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Closing session")

with Session():
    print("Working...")
```

Put cleanup logic in `__exit__()`.

## 5. Generator-based context managers

`contextlib.contextmanager` lets a generator function act as a context manager.

```python
from contextlib import contextmanager

@contextmanager
def session():
    print("Opening session")
    try:
        yield "Session is ready"
    finally:
        print("Closing session")

with session() as value:
    print(value)
```

Output:

```text
Opening session
Session is ready
Closing session
```

Remember:
1. Code before `yield` performs setup.
2. The yielded value is assigned to the `as` variable.
3. Code after `yield` runs as the block exits.

Use `try/finally` around `yield` when cleanup must always happen.

## 6. Exceptions at `yield`

If the `with` block raises an exception, `contextmanager` throws it at the `yield` point. If it is not caught, cleanup runs and the exception propagates.

If the generator catches the exception and finishes normally, it suppresses it:

```python
@contextmanager
def managed():
    try:
        yield
    except ValueError:
        print("Handled")  # Suppresses ValueError
```

To handle/log and still propagate, re-raise:

```python
except ValueError:
    print("Handled")
    raise
```

## 7. File example

`open()` is already a context manager, so use `with open(...)` for ordinary file operations. A custom wrapper may be useful when adding behavior:

```python
from contextlib import contextmanager

@contextmanager
def open_file(filename, mode):
    file = open(filename, mode)
    try:
        yield file
    finally:
        file.close()

with open_file("notes.txt", "w") as file:
    file.write("Learning Python")
```

## 8. AI Engineering connection

Context managers help manage resource lifecycles in file/data processing, backend database sessions, locks, and temporary state. Reliable cleanup is important for robust services and data pipelines.

## Chapter summary

- `with` organizes setup and cleanup.
- Class-based managers implement `__enter__()` and `__exit__()`.
- `__enter__()`'s return value is bound by `as`.
- `__exit__()` runs on normal and exceptional exits.
- `True` suppresses an exception; `False`/`None` lets it propagate.
- `@contextmanager` uses a generator: setup before `yield`, cleanup after it.
- Use `try/finally` to ensure cleanup.
